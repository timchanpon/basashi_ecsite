from django.urls import path

from . import views


app_name = 'orders'
urlpatterns = [
    path('add2-shopping-cart/<int:pk>/<str:from>/', views.AddToShoppingCartView.as_view(), name="add_to_shopping_cart"),
    path('remove-from-shopping-cart/', views.RemoveFromShoppingCartView.as_view(), name="remove_from_shopping_cart"),

    path('fill-order/', views.FillOrderView.as_view(), name="fill_order"),
    path('confirm-order/', views.ConfirmOrderView.as_view(), name="confirm_order"),
    path('create-order/', views.CreateOrderView.as_view(), name="create_order"),
]
