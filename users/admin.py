from django.contrib import admin

from .models import CustomUser, ShoppingCart


admin.site.register(CustomUser)
admin.site.register(ShoppingCart)
