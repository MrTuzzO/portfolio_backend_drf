from rest_framework.generics import ListAPIView
from .models import Education
from .serializers import EducationSerializer


class EducationListView(ListAPIView):
    queryset = Education.objects.all().order_by('-start_date')
    serializer_class = EducationSerializer
