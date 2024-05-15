from django.shortcuts import render, redirect

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')


def login(request):
    return render(request, "login.html")
