from django.views import generic
from django.urls import reverse_lazy

from braces.views import SuperuserRequiredMixin

from .forms import SiteSettingsForm
from .models import SiteSettings


class UpdateSiteSettingsView(SuperuserRequiredMixin, generic.UpdateView):
    model = SiteSettings
    template_name = 'update_site_settings.html'
    form_class = SiteSettingsForm
    slug_field = 'is_selected'
    slug_url_kwarg = 'is_selected'
    success_url = reverse_lazy('posts:post_list')
