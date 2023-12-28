from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/", include("accounts.urls")),
    path("api/posts/", include("posts.urls")),
    path("admin/", admin.site.urls),
]
