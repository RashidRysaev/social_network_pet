from datetime import datetime

from django.utils.timesince import timesince
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.name")
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
