from django.shortcuts import render
from django.contrib import messages
# from .models import Account


def home(request):
    messages.success(request, "Welcome!")
    return render(request, 'home.html')