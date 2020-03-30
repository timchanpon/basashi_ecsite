from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin

from addresses.models import Address
from orders.models import Order
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
        orders = Order.objects.filter(user=user, status='ordered').order_by('-ordered_at')
        # orders_ended = Order.objects.filter(user=user, status='').order_by('-ordered_at')

        context['addresses'] = addresses
        context['orders'] = orders

        return context
