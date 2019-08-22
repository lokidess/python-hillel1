from django import forms

from core.models import Category, Post, Tag


# def get_category_choices():
#     return [
#         (x.id, x.name) for x in Category.objects.all()
#     ]


# class CreatePostForm(forms.Form):
#
#     categories = (
#         (1, 'Travel'),
#         (2, 'Hangover'),
#         (3, 'Bali')
#     )
#
#     title = forms.CharField(required=True, max_length=255, min_length=3, label='Nazvanie posta')
#
#     text = forms.CharField(widget=forms.widgets.Textarea(
#         attrs={'cols': 20, 'rows': 10, 'qwe': 123}
#     ), label='Tekst posta')
#
#     tags = forms.CharField(label='Tegi cherez zapyatuyu')
#
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Ne zadano')
#
#     def __init__(self, *args, **kwargs):
#         super(CreatePostForm, self).__init__(*args, **kwargs)
#         # self.fields['category'].choices = [
#         #     (x.id, x.name) for x in Category.objects.all()
#         # ]
#
#     # def clean(self):
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if 'a' in title:
#             raise forms.ValidationError('Ne nado tak!')
#         return title
#
#     def save(self, user):
#         post = Post.ololo.create(
#             title=self.cleaned_data['title'],
#             text=self.cleaned_data['text'],
#             category=self.cleaned_data['category'],
#             author=user,
#             views_count=100
#         )
#         tags = []
#         for tag in self.cleaned_data['tags'].split(','):
#             tags.append(
#                 Tag.objects.get_or_create(name=tag)[0]
#             )
#
#         post.tags.set(tags)

class CreatePostForm(forms.ModelForm):

    tags = forms.CharField()

    class Meta:
        model = Post
        fields = (
            'title', 'text', 'category', 'preview'
        )

        widgets = {
            'text': forms.widgets.Textarea(attrs={'cols': 20, 'rows': 10})
        }

        labels = {
            'title': 'Nazvanie posta'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'a' in title:
            raise forms.ValidationError('Ne nado tak!')
        return title

    def save(self, user, commit=True):
        post = super(CreatePostForm, self).save(commit=False)
        post.author = user
        post.save()
        tags = []
        for tag in self.cleaned_data['tags'].split(','):
            tags.append(
                Tag.objects.get_or_create(name=tag)[0]
            )

        post.tags.set(tags)
