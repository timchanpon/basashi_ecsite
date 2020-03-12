from django.urls import path

from . import views


app_name = 'post'
urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('create-post/', views.CreatePostView.as_view(), name="create_post"),
    path('delete-post/<int:pk>/', views.DeletePostView.as_view(), name="delete_post"),
]
