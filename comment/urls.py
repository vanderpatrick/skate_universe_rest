from django.urls import path
from comment import views


urlpatterns = [
    path('comments/', views.CommentListView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView().as_view()),
]
