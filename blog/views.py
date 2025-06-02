from django.views.generic import ListView,DetailView
from .models import Post

# List of posts where published
class Post_list(ListView):
    queryset = Post.published.all()
    template_name = 'post_list.html'
    context_object_name = 'posts'

# Detail of posts
class Post_detail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
