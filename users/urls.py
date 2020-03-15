from django.urls import path

from . import views


app_name = 'users'
urlpatterns = [
    path('add2-shopping-cart/<int:pk>/', views.AddToShoppingCartView.as_view(), name="add_to_shopping_cart"),
]
