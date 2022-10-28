from django.urls import path
from Post import views


urlpatterns = [
    path('posts/', views.PostListView.as_view()),
]
