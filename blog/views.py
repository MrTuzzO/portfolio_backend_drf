from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Blog
from .serializers import BlogSerializer, BlogListSerializer


class BlogListView(ListAPIView):
    """List all published blog posts"""
    queryset = Blog.objects.filter(is_published=True).order_by('-published_date')
    serializer_class = BlogListSerializer


class BlogDetailView(RetrieveAPIView):
    """Retrieve a single blog post by slug"""
    queryset = Blog.objects.filter(is_published=True)
    serializer_class = BlogSerializer
    lookup_field = 'slug'
