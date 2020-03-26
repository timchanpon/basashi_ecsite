from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post
from .models import Order


class AddToShoppingCartView(LoginRequiredMixin, generic.View):
    def post(self, request, **kwargs):
        user = self.request.user
        post = Post.objects.get(pk=kwargs['pk'])
        order_amt = request.POST['order_amt']
        tmp = Order(user=user, post=post, order_amt=order_amt)
        tmp.save()

        if kwargs['name'] == 'detail':
            return redirect('posts:post_detail', post.pk)
        else:
            return redirect('posts:post_list')


class RemoveFromShoppingCartView(LoginRequiredMixin, generic.View):
    def post(self, request):
        pk = request.POST['pk']
        user = self.request.user
        order = Order.objects.get(pk=pk)
        if order.user == user:
            order.delete()

        return redirect('posts:post_list')
