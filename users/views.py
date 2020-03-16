from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post
from .models import ShoppingCart


class AddToShoppingCartView(LoginRequiredMixin, generic.View):
    def post(self, request, **kwargs):
        user = self.request.user
        post = Post.objects.get(pk=kwargs['pk'])
        order_amt = request.POST['order_amt']
        tmp = ShoppingCart(user=user, post=post, order_amt=order_amt)
        tmp.save()

        return redirect(reverse('posts:post_list'))


class RemoveFromShoppingCartView(LoginRequiredMixin, generic.View):
    def post(self, request):
        pk = request.POST['pk']
        user = self.request.user
        shopping_cart = ShoppingCart.objects.get(pk=pk)
        if shopping_cart.user == user:
            shopping_cart.delete()

        return redirect(reverse('posts:post_list'))
