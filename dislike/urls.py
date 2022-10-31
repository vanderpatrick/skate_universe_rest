from django.urls import path
from dislike import views


urlpatterns = [
    path('dislikes/', views.DislikeListView.as_view()),
    path('profiles/<int:pk>/', views.DislikeDetailView.as_view()),
]
