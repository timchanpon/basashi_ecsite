from django.urls import path

from . import views


app_name = 'addresses'
urlpatterns = [
    path('add-address', views.AddAddressView.as_view(), name="add_address"),
]
