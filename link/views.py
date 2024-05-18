from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('dashboard')

@login_required
def dashboard(request):
    return render(request, "dashboard.html")