from django.urls import path

from .api import post_list, post_create, post_list_profile


urlpatterns = [
    path("", post_list, name="post-list"),
    path("profile/<uuid:id>/", post_list_profile, name="post-list-profile"),
    path("create/", post_create, name="post-create"),
]
