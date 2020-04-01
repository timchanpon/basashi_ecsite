from django.urls import path

from . import views


app_name = 'users'
urlpatterns = [
    path('user-detail/<int:pk>/', views.UserDetailView.as_view(), name="user_detail"),
    path('update-user/', views.UpdateUserView.as_view(), name="update_user"),
]
