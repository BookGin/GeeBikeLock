from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django import forms


def home(request):
    if not request.user.is_authenticated():
        return redirect(reverse('login'))
    return render(request, 'home.html')

def landing_page(request):
    if request.user.is_authenticated():
        return redirect(reverse('index'))
    return redirect(reverse('login'))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form, })



