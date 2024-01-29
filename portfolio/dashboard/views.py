from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Dashboard, About, Skills, Project, ContactMe
from .forms import ContactMeForm


# Dashboard
def dashboard(request):
    items = Dashboard.objects.all()
    return render(request, 'dashboard/dashboard.html', {'items': items, 'title': 'Home'})


# About
def about(request):
    items = About.objects.all()
    return render(request, 'dashboard/about.html', {'items': items})


# Skills
def skills(request):
    skills = Skills.objects.all()
    return render(request, 'dashboard/skills.html', {'skills': skills})


# Projects
def portfolio_projects(request):
    projects = Project.objects.all()
    return render(request, 'dashboard/portfolio_projects.html', {'projects': projects})


# Contact Me
def contact_me(request):
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, f'Your message was sent successfully.')
            return redirect('contact-me')
    else:
        form = ContactMeForm()
    return render(request, 'dashboard/contactme.html', {'form': form})
