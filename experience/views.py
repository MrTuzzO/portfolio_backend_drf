from rest_framework.generics import ListAPIView
from .models import WorkExperience
from .serializers import WorkExperienceSerializer


class WorkExperienceListView(ListAPIView):
    queryset = WorkExperience.objects.select_related().prefetch_related('technologies').order_by('-starting_date')
    serializer_class = WorkExperienceSerializer
