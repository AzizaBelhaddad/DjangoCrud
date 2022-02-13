from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .models import Profile


# Create your views here.

def listprofiles(request):
    profiles = Profile.objects.filter(state=1)
    return render(request, 'account/profiles.html', {'profiles': profiles})


def showProfile(request, id):
    profile = Profile.objects.get(pk=id)
    return render(request,'account/showProfile.html', {'profile': profile})

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('list_articles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except :
            messages.warning(request,"This username doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'login success')
            return redirect('list_articles')
        else:
            messages.warning(request,'username or password is incorrect')


    return render(request, "account/login.html", {'page': 'login'})

def logoutUser(request):
    logout(request)
    # messages.info(request, "your no more connected")
    return redirect('login')


def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        if form.is_valid:
            user = form.save()
            messages.info(request, 'account successfully created')
            login(request, user)
            return redirect('list_article')

    data = {'form': form, 'page': 'Register'}
    return render(request, template_name='account/login.html',context = data)