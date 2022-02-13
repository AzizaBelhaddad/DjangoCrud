from django.urls import path
from .views import loginUser, logoutUser, registerUser, showProfile, listprofiles

urlpatterns = [
    path("login/", loginUser, name = "login"),
    path("logout/", logoutUser, name = "logout"),
    path("register/", registerUser, name = "register"),
 
    path("showProfile/", showProfile, name = "showProfile"),
    path("profiles/", listprofiles, name = "list_Profiles"),


    



]