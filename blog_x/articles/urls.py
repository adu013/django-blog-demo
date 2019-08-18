from django.urls import path, re_path

from .views import articleListView, articleDetailView, articleCreateView, articleEditView

app_name = 'articles'

urlpatterns = [
    path('', articleListView, name='article_list'),
    path('create/', articleCreateView, name='article_create'),
    re_path(r'^(?P<slug>[\w-]+)/$', articleDetailView, name='article_detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', articleEditView, name='article_edit'),
]
