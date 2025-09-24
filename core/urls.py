from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('site-content/', views.SiteContentView.as_view(), name='site-content'),
    path('social-links/', views.SocialLinkListView.as_view(), name='social-links'),
]
