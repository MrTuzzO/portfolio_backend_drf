from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.pagination import DefaultPagination
from .models import Project, ProjectCategory
from .serializers import (
    ProjectListSerializer, 
    ProjectDetailSerializer, 
    ProjectCategorySerializer
)


class ProjectCategoryListView(ListAPIView):
    """List all project categories"""
    queryset = ProjectCategory.objects.all().order_by('name')
    serializer_class = ProjectCategorySerializer


class ProjectListView(ListAPIView):
    """List all projects with filtering by category"""
    queryset = Project.objects.select_related('category').prefetch_related('technologies').all()
    serializer_class = ProjectListSerializer
    pagination_class = DefaultPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category', None)
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset.order_by('-id')  # Most recent first


class ProjectDetailView(RetrieveAPIView):
    """Retrieve a single project"""
    queryset = Project.objects.select_related('category').prefetch_related('technologies').all()
    serializer_class = ProjectDetailSerializer


@api_view(['GET'])
def projects_by_category(request):
    """Get projects grouped by category"""
    categories = ProjectCategory.objects.prefetch_related('projects__technologies').all()
    
    result = []
    for category in categories:
        projects = ProjectListSerializer(
            category.projects.all(), 
            many=True,
            context={'request': request}
        ).data
        
        result.append({
            'id': category.id,
            'name': category.name,
            'projects': projects,
            'projects_count': len(projects)
        })
    
    return Response(result)
