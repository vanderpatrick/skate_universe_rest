from django.urls import path
from Follower import views


urlpatterns = [
    path('followers/', views.FollowerListView.as_view()),
    path('followers/<int:pk>/', views.FollowerDetailView.as_view()),
]
