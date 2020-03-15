from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse

from posts.models import Post
from .models import ShoppingCart


class AddToShoppingCartView(generic.View):
    def post(self, request, **kwargs):
        user = self.request.user
        post = Post.objects.get(pk=kwargs['pk'])
        order_amt = request.POST['order_amt']
        tmp = ShoppingCart(user=user, post=post, order_amt=order_amt)
        tmp.save()

        return redirect(reverse('posts:post_list'))
