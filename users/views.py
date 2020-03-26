from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin

from addresses.models import Address
from .models import CustomUser


class UserDetailView(UserPassesTestMixin, generic.DetailView):
    model = CustomUser
    template_name = 'user_detail.html'

    def test_func(self):
        user = self.request.user

        return user.pk == self.kwargs['pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        addresses = Address.objects.filter(user=user)
        context['addresses'] = addresses

        return context
