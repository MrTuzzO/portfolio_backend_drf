from django.urls import path
from . import views

urlpatterns = [
    path('work-experience/', views.WorkExperienceListView.as_view(), name='work-experience'),
]