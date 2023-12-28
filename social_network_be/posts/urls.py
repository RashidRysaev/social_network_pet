from django.urls import path

from .api import post_list, post_create


urlpatterns = [
    path("", post_list, name="post-list"),
    path("create/", post_create, name="post-create"),
]
