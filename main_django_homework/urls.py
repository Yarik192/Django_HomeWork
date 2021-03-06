"""main_django_homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="homepage"),
    path("articles/", articles, name="articles"),
    path("articles/archive/", archive_a, name="articles_archive"),
    path("users/", users, name="users"),
    path("comments", view_comments, name="comments"),
    path("article/<int:article_num>/", article_int, name="article_num"),
    path("article/<int:article_num>/archive", article_in_archive, name="article_num_archive"),
    path("article/<int:article_num>/<slug:slug_text>", article_slug, name="article_slug"),
    path("users/<int:user_num>/", users_num, name="user_num"),
    re_path(r"^(?P<url>\d{2}[a-zA-Z]\d[-]......$)", re_url, name="re_url"),
    path("<str:phone>", phone, name="valid_phone"),
]
