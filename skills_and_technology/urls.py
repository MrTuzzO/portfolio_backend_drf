from django.urls import path
from . import views

urlpatterns = [
    path('st-categories/', views.STCategoryListView.as_view(), name='categories'),
    path('skills-and-technologies/', views.SkillAndTechnologyListView.as_view(), name='skills'),
]