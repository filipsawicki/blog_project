from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'


class BlogDetalView(DetailView):
    model = Post
    template_name = 'post_detail.html'
