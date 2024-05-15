from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from link import forms
from django.contrib.auth import authenticate, login as authLogin

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('dashboard')


def login(request):
    form = forms.LoginForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data["email"],
                                password=form.cleaned_data["password"])
            if user is not None:
                authLogin(request, user)
                response = HttpResponse()
                response["HX-Redirect"] = reverse("dashboard")
                return response
            else:
                form.add_error("password", "Invalid email or password")
        return render(request, "forms/login-form.html", {"loginForm": form})

    return render(request, "login.html")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")