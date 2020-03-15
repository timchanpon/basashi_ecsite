from django.views import generic
from django.urls import reverse_lazy

from posts.models import Post
from .models import ShoppingCart


class AddToShoppingCartView(generic.View):
    def post(self, request):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        order_amt = request.POST['order_amt']
        tmp = ShoppingCart(user=user, post=post, order_amt=order_amt)
        tmp.save()

        return reverse_lazy('posts:post_list')
