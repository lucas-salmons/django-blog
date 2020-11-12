from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

class BlogListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    template_name = 'blogging/list.html'

class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = 'blogging/detail.html'

    