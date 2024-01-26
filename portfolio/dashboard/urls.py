from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('portfolio_projects/', views.portfolio_projects, name='portfolio-projects'),
]