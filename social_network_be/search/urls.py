from django.urls import path

from .api import search_view


urlpatterns = [
    path("", search_view, name="search"),
]
