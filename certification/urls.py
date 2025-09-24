from django.urls import path
from . import views

urlpatterns = [
    path('certifications/', views.CertificationListView.as_view(), name='certification-list'),
]
