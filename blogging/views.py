from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)

class BlogListView(ListView):
    pass

class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = 'blogging/detail.html'
    

    