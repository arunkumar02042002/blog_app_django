from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    queryset = Post.objects.all().order_by('-created_at')
    template_name = "blog/home.html"
    context_object_name = 'blog_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = 'blog'