from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

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
        orders = Order.objects.filter(user=user, has_ended=False).order_by('-ordered_at')
        orders_ended = Order.objects.filter(user=user, has_ended=True).order_by('-ended_at')

        context['addresses'] = addresses
        context['orders'] = orders
        context['orders_ended'] = orders_ended

        return context


class UpdateUserView(LoginRequiredMixin, generic.View):
    def post(self, request):
        user = self.request.user
        if 'user_icon' in request.FILES:
            user.user_icon = request.FILES['user_icon']
            user.save()
        elif 'reset_user_icon' in request.POST:
            user.user_icon = request.POST['reset_user_icon']
            user.save()
        elif 'username' in request.POST:
            user.username = request.POST['username']
            user.save()

        return redirect('users:user_detail', user.pk)
