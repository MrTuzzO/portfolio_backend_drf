from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import SiteContent, SocialLink
from .serializers import SiteContentSerializer, SocialLinkSerializer


class SiteContentView(RetrieveAPIView):
    serializer_class = SiteContentSerializer
    
    def get_object(self):
        return SiteContent.get_instance()


class SocialLinkListView(ListAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer