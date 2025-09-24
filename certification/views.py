from rest_framework.generics import ListAPIView
from .models import Certification
from .serializers import CertificationSerializer


class CertificationListView(ListAPIView):
    queryset = Certification.objects.all().order_by('-issue_date')
    serializer_class = CertificationSerializer
