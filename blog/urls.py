from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blogs/', views.BlogListView.as_view(), name='blog-list'),
    path('blogs/<slug:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
]
