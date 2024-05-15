from django.urls import path
from link import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
]