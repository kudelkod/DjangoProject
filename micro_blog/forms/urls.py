from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.form),
    # re_path(r'^test_view/$', views.test_view),
    re_path(r'^search/$', views.search),
    re_path(r'^add-author/$', views.author_add),
    re_path(r'^add-article/$', views.article_add),
    re_path(r'^search-form/$', views.search_form),
    re_path(r'^file-input/$', views.file_input),
]
