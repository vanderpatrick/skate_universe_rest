from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

post_categorys = [
    ('gaps', 'Gaps'),
    ('rails', 'Rail'),
    ('ledges', 'Ledges'),
    ('street', 'Street')
]


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_qdjgyp', blank=True)

    post_category_filter = models.CharField(
        max_length=50, choices=post_categorys, default='normal'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.id} {self.title}'
