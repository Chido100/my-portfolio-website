from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('portfolio_projects/', views.portfolio_projects, name='portfolio-projects'),
    path('contact_me/', views.contact_me, name='contact-me'),
]