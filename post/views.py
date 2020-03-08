from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')
