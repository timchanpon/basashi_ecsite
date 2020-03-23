from django.contrib import admin

from .models import Prefecture, City, Chome, Address


admin.site.register(Prefecture)
admin.site.register(City)
admin.site.register(Chome)
admin.site.register(Address)
