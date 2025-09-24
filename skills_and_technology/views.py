from rest_framework.generics import ListAPIView
from .models import STCategory, SkillAndTechnology
from .serializers import STCategorySerializer, SkillAndTechnologySerializer


class STCategoryListView(ListAPIView):
    queryset = STCategory.objects.all()
    serializer_class = STCategorySerializer


class SkillAndTechnologyListView(ListAPIView):
    queryset = SkillAndTechnology.objects.all()
    serializer_class = SkillAndTechnologySerializer
