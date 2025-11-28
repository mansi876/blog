from django.views.generic import ListView, DetailView
from .models import Post, Category

class BlogListView(ListView):
    model = Post
    template_name = 'blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status='published')

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'post'
