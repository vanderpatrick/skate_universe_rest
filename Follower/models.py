from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['author', 'followed']

    def __str__(self):
        return f"{self.author} has followed {self.followed}"
