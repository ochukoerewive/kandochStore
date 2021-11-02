from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Vendor
# Create your views here.

def index(request):
    """ A view to return the index page"""
    return render(request, 'home/index.html')

def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name=user.username, created_by=user)

            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'home/become_vendor.html', {'form': form})