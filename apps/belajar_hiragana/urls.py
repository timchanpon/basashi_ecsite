from django.urls import path

from .views import HomeView, WordAPIView


urlpatterns = [
    path('', HomeView.as_view()),
    path('api/<int:word_count>/<str:pk>/', WordAPIView.as_view()),
]
