from django.urls import path

from . import views


app_name = 'common'
urlpatterns = [
    path('update-site-settings/<is_selected>/', views.UpdateSiteSettingsView.as_view(), name="update_site_settings"),
]
