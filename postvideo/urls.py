from django.urls import path
from postvideo import views


urlpatterns = [
    path('video_posts/', views.VideoPostListView.as_view()),
    path('video_posts/<int:pk>/', views.VideoPostDetailView.as_view()),
]