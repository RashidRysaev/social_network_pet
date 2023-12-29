import uuid

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.decorators import api_view

from accounts.serializers import UserSerializer

from .models import Post
from .serializers import PostSerializer


@api_view(["GET"])
def post_list(request) -> "JsonResponse":
    posts = Post.objects.order_by("-created_at")
    data = PostSerializer(posts, many=True).data
    return JsonResponse(data, safe=False)


@api_view(["GET"])
def post_list_profile(request, id: uuid) -> "JsonResponse":
    posts = Post.objects.filter(created_by__id=id)
    posts_data = PostSerializer(posts, many=True).data

    user = get_user_model().objects.get(id=id)
    user_data = UserSerializer(user).data

    return JsonResponse({"posts": posts_data, "user": user_data}, safe=False)


@api_view(["POST"])
def post_create(request):
    user = get_user_model().objects.get(id=request.user.id)
    post_data = Post.objects.create(body=request.data.get("body"), created_by=user)
    data = PostSerializer(post_data).data
    return JsonResponse(data)
