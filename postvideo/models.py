from django.db import models
from django.contrib.auth.models import User

post_categorys = [
    ('gaps', 'Gaps'),
    ('rails', 'Rail'),
    ('ledges', 'Ledges'),
    ('street', 'Street')
]


class VideoPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    video = models.FileField(
        upload_to='videos/',
        null=True)
    post_categorys_filter = models.CharField(
        max_length=50, choices=post_categorys, default='normal'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
