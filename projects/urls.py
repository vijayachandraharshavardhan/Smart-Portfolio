from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('projects/', views.project_list, name='projects'),
    path('about/', views.about, name='about'),
]
