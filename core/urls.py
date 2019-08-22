"""one_more_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from core.views import IndexView, index_view, AboutView, UsersView, UserView, CreatePostView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('about/', AboutView.as_view(), name='about'),
    # path('rrr/', FeedbackView.as_view(), name='feedback'),
    path('all-users/', UsersView.as_view(), name='all_users'),
    path('account/<int:pk>/', UserView.as_view(), name='user_detail'),
    # url('^(?P<username>[-\w]+)/$', IndexView.as_view())
]
