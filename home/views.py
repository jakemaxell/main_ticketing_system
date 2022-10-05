from django.shortcuts import render
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, "home.html", {})