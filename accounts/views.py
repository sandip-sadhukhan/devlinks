from django.shortcuts import render
from accounts import forms
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from accounts.models import User

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
                user_exists = User.objects.filter(email=form.cleaned_data["email"]).exists()

                if user_exists:
                    form.add_error("password", "Please check again")
                else:
                    form.add_error("email", "User does not exist")

        return render(request, "forms/login-form.html", {"loginForm": form})

    return render(request, "login.html")

def signup(request):
    form = forms.SignupForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            if User.objects.filter(email=email).exists():
                form.add_error("email", "User already exists")
            else:
                username = User.generate_username(email)
                user = User.objects.create_user(username=username, email=email,
                                                password=password)
                authLogin(request, user)
                response = HttpResponse()
                response["HX-Redirect"] = reverse("dashboard")
                return response
        return render(request, "forms/signup-form.html", {"signupForm": form})

    return render(request, "signup.html")

def logout(request):
    authLogout(request)
    return redirect("login")