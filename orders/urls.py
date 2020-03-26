from django.urls import path

from . import views


app_name = 'orders'
urlpatterns = [
    path('add2-shopping-cart/<int:pk>/<str:name>/', views.AddToShoppingCartView.as_view(), name="add_to_shopping_cart"),
    path('remove-from-shopping-cart/', views.RemoveFromShoppingCartView.as_view(), name="remove_from_shopping_cart"),
]
