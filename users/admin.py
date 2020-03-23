from django.contrib import admin

from .models import Prefecture, City, Chome, CustomUser, ShoppingCart


admin.site.register(CustomUser)
admin.site.register(ShoppingCart)

admin.site.register(Prefecture)
admin.site.register(City)
admin.site.register(Chome)
