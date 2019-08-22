from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.shortcuts import render
# from core.forms import TestForm
from django.urls.base import reverse_lazy
from django.db.models.query_utils import Q
from django.db.models import F
from django.db.models.aggregates import Sum
from django.contrib.auth import get_user_model

from core.models import Post, Tag, Category

from core.forms import CreatePostForm
from django.shortcuts import redirect


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        print('POST')


# class IndexView(CreateView):
#     template_name = 'index.html'
#     form_class = TestForm
#     success_url = '/'

class IndexView(View):

    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        # print(username)
        # request is self.request  # True
        # request.GET
        # user = User.objects.get(username='admin')
        # posts = Post.objects.filter(author=user)
        # posts = Post.objects.all().select_related(
        #     'author'
        # ).prefetch_related(
        #     'tags'
        # )

        # Post.objects.filter(author=user).update(
        #     title='Good plan!')

        # post = Post.objects.create(
        #     text='Trololo',
        #     title='Loki jokes',
        #     author=user,
        #     category_id=1
        # )

        # post = Post.objects.get(id=4)
        #
        # post.tags.add(Tag.objects.get(id=1))

        # for post in posts:
        #     print(post.tags.all())

        # post = Post.objects.get(id=1)
        # post.title = 'Yaba aba'
        # post.save()

        # posts = Post.objects.all().exclude(title='Good plan')

        # posts = Post.objects.all().first()

        # posts = Post.objects.all().order_by('title').first()

        # .....

        # posts = posts.filter(author=user)

        # posts = Post.objects.filter(author__email='loki@loki.com').select_related()
        # posts = Post.objects.filter(title__startswith='Good')
        # posts = Post.objects.filter(title__contains='PL')

        # posts = Post.objects.filter(title__istartswith='Good')
        # posts = Post.objects.filter(title__icontains='PL')
        # filters = Q()

        # filters.add(Q.OR, title__startswith='Good')

        # posts = Post.objects.filter(
        #     Q(title__startswith='Good') &
        #     Q(title__contains='pl') &
        #     ~Q(author__username='loki')
        # ).distinct()

        # posts = Post.objects.filter(
        #     title=F('author__username')
        # )

        # posts = Post.objects.filter(tags__name='сказочноебали')
        # for post in posts:
        #     print(post.id)
        # print(posts)
        # counts = 0
        # for post in Post.objects.all():
        #     counts += post.views_count

        # counts = Post.objects.using('default').aggregate(Sum('views_count'))

        # counts = Post.objects.using('default').all()
        # counts2 = Post.objects.using('posts').all()
        #
        # counts = counts | counts2

        # counts = {}
        # for post in Post.objects.all():
        #     if post.author.username in counts:
        #         counts[post.author.username] += post.views_count
        #     else:
        #         counts[post.author.username] = post.views_count

        # counts = User.objects.annotate(views_count=Sum('post__views_count')).values(
        #     'username', 'views_count'
        # )

        # counts = User.objects.using('default').annotate(views_count=Sum('post__views_count')).order_by(
        #     '-views_count'
        # ).filter(views_count__gt=10)
        # print(counts)
        posts = Post.ololo.all()
        context = {
            'first': 123,
            'second': 321,
            'posts': posts
        }
        return render(request, 'index.html', context=context)

    def post(self, request):
        # request.POST
        return render(request, 'index.html')


class AboutView(TemplateView):
    template_name = 'about.html'

    # def get(self, request, *args, **kwargs):
    #     pass
    #     # return
    #
    # def render_to_response(self, context, **response_kwargs):
    #     pass
    #
    # def get_context_data(self, **kwargs):
    #     pass


# class FeedbackView(FormView):
#     template_name = 'feedback.html'
#     form_class = TestForm
#     success_url = reverse_lazy('core:feedback')
#
#     def form_valid(self, form):
#         print('Valid')
#         # self.request
#         # self.kwargs
#         return super(FeedbackView, self).form_valid(form)
#
#     def form_invalid(self, form):
#         print('Invalid')
#         return super(FeedbackView, self).form_invalid(form)

#

# class FeedbackView(View):
#
#     def get(self, request):
#         context = {
#             'form': TestForm()
#         }
#         return render(request, 'feedback.html', context)
#
#     def post(self, request):
#         form = TestForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             print('Valid')
#         else:
#             print('Invalid')
#
#         context = {
#             'form': form
#         }
#         return render(request, 'feedback.html', context)


class UsersView(ListView):
    queryset = get_user_model()
    template_name = 'all_users.html'
    paginate_by = 10

    # def get_queryset(self):
    #     pass


class UserView(DetailView):
    template_name = 'user_profile.html'
    model = get_user_model()
    # slug_url_kwarg = 'username'
    # slug_field = 'username'

    # def get_object(self, queryset=None):
    #     pass


class CreatePostView(TemplateView):
    template_name = 'create_post.html'

    def get_context_data(self, **kwargs):
        context = super(CreatePostView, self).get_context_data(**kwargs)
        context['form'] = CreatePostForm()
        return context

    def post(self, request):
        form = CreatePostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(request.user)
            return redirect('/')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


# class CreatePostView(FormView):
#     template_name = 'create_post.html'
#     form_class = CreatePostForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         form.save(self.request.user)
#         return super(CreatePostView, self).form_valid(form)

# class CreatePostView(CreateView):
#     model = Post
#     success_url = '/'
#     fields = '__all__'
#     template_name = 'create_post.html'
