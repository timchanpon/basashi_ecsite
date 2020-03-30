from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Address


class AddAddressView(LoginRequiredMixin, generic.View):
    def post(self, request, **kwargs):
        user = self.request.user
        pref = request.POST['pref']
        city = request.POST['city']
        chome = request.POST['chome']
        banchi_go = request.POST['banchi_go']

        tmp = Address(user=user, pref=pref, city=city, chome=chome, banchi_go=banchi_go)
        if request.POST['building']:
            building = request.POST['building']
            tmp.building = building
        if request.POST['address_type']:
            address_type = request.POST['address_type']
            tmp.address_type = address_type

        tmp.save()

        if kwargs['from'] == 'user_detail':
            return redirect('users:user_detail', user.pk)
        elif kwargs['from'] == 'fill_order':
            return redirect('orders:fill_order')
