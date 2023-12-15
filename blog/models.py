from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from common.models import TimeStampModel

User = get_user_model()

# Create your models here.
class Post(TimeStampModel):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    thumbnail = models.ImageField(upload_to='blog/thumnails', default='no-thumbnail.jpeg')
    description = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.author_id) + '-' + self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})