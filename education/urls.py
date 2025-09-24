from django.urls import path
from . import views

urlpatterns = [
    path('education/', views.EducationListView.as_view(), name='education-list'),
]
