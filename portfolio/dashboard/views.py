from django.shortcuts import render, redirect, get_object_or_404
from .models import Dashboard, About, Experience, Project


# Dashboard
def dashboard(request):
    items = Dashboard.objects.all()
    return render(request, 'dashboard/dashboard.html', {'items': items, 'title': 'Home'})


# About
def about(request):
    items = About.objects.all()
    return render(request, 'dashboard/about.html', {'items': items})


# Experience
def experience(request):
    items = Experience.objects.all()
    return render(request, 'dashboard/experience.html', {'items': items})


# Projects
def portfolio_projects(request):
    projects = Project.objects.all()
    return render(request, 'dashboard/portfolio_projects.html', {'projects': projects})