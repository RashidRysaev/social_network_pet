from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework.decorators import api_view

from accounts.serializers import UserSerializer
from posts.models import Post
from posts.serializers import PostSerializer


@api_view(["POST"])
def search_view(request):
    data = request.data
    query = data["query"]

    user_qs = get_user_model().objects.filter(name__icontains=query)
    user_data = UserSerializer(user_qs, many=True).data

    post_qs = Post.objects.filter(body__icontains=query)
    post_data = PostSerializer(post_qs, many=True).data

    return JsonResponse({"users": user_data, "posts": post_data}, safe=False)
