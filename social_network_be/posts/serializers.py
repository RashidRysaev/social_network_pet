from datetime import datetime

from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "body",
            "created_by",
            "created_at",
        )

    def get_created_at(self, obj: Post) -> datetime:
        return timesince(obj.created_at)
