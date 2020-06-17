from django.urls import re_path
from . import views

urlpatterns = [
    re_path("123/", views.hello),
    re_path("456/", views.world, name="main_page"),
    re_path("comment/(?P<id>\d+)/", views.accept_comment, name="add_comment"),
    re_path("one_video/(?P<id>\d+)/", views.one_video, name="one_video"),
    re_path("add_like/(?P<id>\d+)/", views.add_like),
    re_path("ajax/add_like/", views.ajax_like),
    # re_path("ajax/comment_add/(?P<id>\d+)/", views.ajax_comment_add, name="comment_add"),
]
