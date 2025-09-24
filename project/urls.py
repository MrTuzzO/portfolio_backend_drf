from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    # Category URLs
    path('categories/', views.ProjectCategoryListView.as_view(), name='category-list'),
    
    # Project URLs
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    
    # Combined view
    path('projects-by-category/', views.projects_by_category, name='projects-by-category'),
]
