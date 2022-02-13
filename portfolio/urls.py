from django.urls import path
from .views import  showProject,listprojects, showProfileProject

urlpatterns = [
    
    path("showProject/", showProject, name = "showProject"),
    path("projects/", listprojects, name = "list_Projects"),
    path("showProfileProject/", showProfileProject, name = "Projects_By_Profile"),


    



]