from django.urls import path
from link import views

urlpatterns = [
    path("", views.index, name="index")
]