import uuid

from django.contrib.auth import get_user_model
from django.db import models


class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="post_attachments")


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    attachment = models.ManyToManyField(to=PostAttachment, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=get_user_model(), related_name="posts", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title

    @property
    def title(self) -> str:
        return self.body[:10]
