from django.urls import path
from postvideo import views


urlpatterns = [
    path('video_posts/', views.VideoPostListView.as_view()),
    # path('posts/<int:pk>/', views.PostDetailView.as_view()),
]