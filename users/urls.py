from django.urls import path

from . import views


app_name = 'users'
urlpatterns = [
    path('user-detail/<int:pk>/', views.UserDetailView.as_view(), name="user_detail"),
    path('update-username/', views.UpdateUsernameView.as_view(), name="update_username"),
]
