from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
from .models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import registerationForm, loginForm

# Create your views here.
def homePage(request):
    return render(request, 'passwordStroage/home.html')

def registeration(request):
    form = registerationForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect(homePage)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data("password1")
        try:
            user = User.objects.create_user(username,email,password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect(user_pw_all)
        else:
            request.session["register_error"] = 1
    return render(request, "passwordStroage/account/register.html", {"form" : form})

def loginPage(request):
    form = loginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect(homePage)
    username = form.cleaned_data.get("username")
    password = form.cleaned_data("password")
    user = authenticate(request, username=username, password=password)
    if user != None:
        login(request, user)
        return redirect(user_pw_all)
    else:
        return render(request, "passwordStroage/account/login.html", {"form" : form})

@login_required(login_url=loginPage)
def logoutPage(request):
    logout(request)
    return render(request, 'passwordStroage/account/logout.html')