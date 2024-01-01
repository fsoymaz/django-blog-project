from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout #kullanıcı var mı yok mu


# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        login(request, new_user)
        messages.info(request, 'Başarıyla kayıt olundu')
        return redirect('index')
    context = {"form": form}
    return render(request, "register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Username or Password is mistake')
            return render(request, "login.html", context)

        messages.success(request, 'Login Successful')
        login(request, user)
        return redirect('index')
    return render(request, "login.html", context)

    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    messages.success(request, 'Başarıyla çıkış yaptınız')
    return redirect('index')
