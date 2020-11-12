from django.urls import path
from blogging.views import list_view, BlogDetailView

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),
]