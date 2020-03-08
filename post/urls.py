from django.urls import path

from . import views


app_name = 'post'
urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path('create-post/', views.CreatePostView.as_view(), name="create_post")
]
