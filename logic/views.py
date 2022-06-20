from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, PostsForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Businesses, Neighbourhood, Profile, Posts

# Create your views here.

def login_request(request):
    form = LoginForm(request.POST)
    if request.POST:
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect('home')
        else:
            context = {
                'form': form,
                'valid': 'was-validated'
            }
        return render(request, 'auth/login.html', context=context)
    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context=context)

