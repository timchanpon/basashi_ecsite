from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from addresses.models import Address
from posts.models import Post
from .models import CustomUser, ShoppingCart


class AddToShoppingCartView(LoginRequiredMixin, generic.View):
    def post(self, request, **kwargs):
        user = self.request.user
        post = Post.objects.get(pk=kwargs['pk'])
        order_amt = request.POST['order_amt']
        tmp = ShoppingCart(user=user, post=post, order_amt=order_amt)
        tmp.save()

        return redirect('posts:post_list')


class RemoveFromShoppingCartView(LoginRequiredMixin, generic.View):
    def post(self, request):
        pk = request.POST['pk']
        user = self.request.user
        shopping_cart = ShoppingCart.objects.get(pk=pk)
        if shopping_cart.user == user:
            shopping_cart.delete()

        return redirect('posts:post_list')


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        addresses = Address.objects.filter(user=user)
        context['addresses'] = addresses

        return context
