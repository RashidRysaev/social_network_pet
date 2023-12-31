from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("accounts.urls")),
    path("api/posts/", include("posts.urls")),
    path("api/search/", include("search.urls")),
]
