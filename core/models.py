from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.aggregates import Sum
from django.contrib.auth import get_user_model

from django.db.models.signals import pre_save
from django.dispatch import receiver

# class TestModel(models.Model):
#     test_field = models.CharField(max_length=10)
#     test_integer = models.IntegerField()


def folder_avatar(obj):
    return f'avatars/{obj.username}'


class MyUser(AbstractUser):
    avatar = models.ImageField(upload_to=folder_avatar)
    phone = models.CharField(max_length=11)


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class PostManager(models.Manager):

    def all_posts_views_count(self):
        queryset = self.get_queryset()
        return queryset.aggregate(views_count=Sum('views_count'))['views_count']

    def get_published(self):
        queryset = self.get_queryset()
        return queryset.filter(published_at__isnull=False)


class Post(TimeStamp):
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField('core.Tag')
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)

    views_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)

    preview = models.ImageField(upload_to='post/preview')

    ololo = PostManager()

    # class Meta:
    #     ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author}"

    def save(self, *args, **kwargs):
        # Before save
        # self.title = 'Haha! Evil signal logic!'
        super(Post, self).save(*args, **kwargs)
        # After save


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# @receiver(pre_save, sender=Post)
# def post_save_handler(sender, instance, **kwargs):
#     instance.title = 'Haha! Evil signal logic!'
