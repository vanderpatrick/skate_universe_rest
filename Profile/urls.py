from django.urls import path
from Profile import views


urlpatterns = [
    path('profiles/', views.ProfileListView.as_view()),
    path('profiles/<int:pk>', views.ProfileDetail.as_view()),
]
