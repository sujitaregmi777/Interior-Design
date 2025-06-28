from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'design/index.html')

def about(request):
    return render(request, 'design/about.html')

def features(request):
    return render(request, 'design/features.html')

def work(request):
    return render(request, 'design/work.html')

def contact(request):
    return render(request, 'design/contact.html')

def login(request):
    form = AuthenticationForm()
    return render(request, 'design/login.html', {'form': form})

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'design/register.html', {'form': form})

# Create your views here.
