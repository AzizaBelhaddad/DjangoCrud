from django.shortcuts import render

from .models import Project

# Create your views here.

def listprojects(request):
    profiles = Project.objects.filter(state=1)
    return render(request, 'account/profiles.html', {'profiles': profiles})


def showProject(request, id):
    profile = Project.objects.get(pk=id)
    return render(request,'account/showProfile.html', {'profile': profile})

def showProfileProject(request, profile):
    profile_projects = Project.objects.filter(profile=profile)
    return render(request,'account/showProfile.html', {'profProj': profile_projects})