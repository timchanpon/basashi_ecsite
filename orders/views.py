from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post
from addresses.models import Address
from .models import OrderItem


class AddToShoppingCartView(LoginRequiredMixin, generic.View):
    def post(self, request, **kwargs):
        user = self.request.user
        post = Post.objects.get(pk=kwargs['pk'])
        order_amt = request.POST['order_amt']
        tmp = OrderItem(user=user, post=post, order_amt=order_amt)
        tmp.save()

        if kwargs['name'] == 'detail':
            return redirect('posts:post_detail', post.pk)
        else:
            return redirect('posts:post_list')


class RemoveFromShoppingCartView(LoginRequiredMixin, generic.View):
    def post(self, request):
        pk = request.POST['pk']
        user = self.request.user
        order = OrderItem.objects.get(pk=pk)
        if order.user == user:
            order.delete()

        return redirect('posts:post_list')


class FillOrderView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'fill_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        address_list = Address.objects.filter(user=user)

        context['address_list'] = address_list

        return context


class ConfirmOrderView(LoginRequiredMixin, generic.View):
    def post(self, request):
        user = self.request.user
        address_pk = request.POST['address_pk']

        cart_obj_list = OrderItem.objects.filter(user=user, in_cart=True)
        address = Address.objects.get(pk=address_pk, user=user)

        context = {
            'cart_obj_list': cart_obj_list,
            'address': address,
        }

        return render(request, 'confirm_order.html', context)
