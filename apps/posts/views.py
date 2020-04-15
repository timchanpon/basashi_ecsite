from django.views import generic
from django.urls import reverse_lazy

from braces.views import SuperuserRequiredMixin

from .forms import PostForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreatePostView(SuperuserRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.stock_amt = form.cleaned_data['purchase_amt']
        post.save()

        return super().form_valid(form)


class DeletePostView(SuperuserRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts:post_list')
