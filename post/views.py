from django.views import generic
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


class CreatePostView(generic.CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('post:post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.stock_amt = form.cleaned_data['purchase_amt']
        post.save()

        return super().form_valid(form)
