from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as django_logout


def index(request):
    return render(request, 'design/index.html')

def about(request):
    return render(request, 'design/about.html')

def features(request):
    return render(request, 'design/features.html')

def work(request):
    return render(request, 'design/work.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'design/contact.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user) 
                messages.success(request, ("You are logged in!!")) 
                return redirect('index')   
            else:
                messages.success(request, ("Error in logging!!")) 
                return redirect('login')                   
    else:
        form = AuthenticationForm()
        # messages.success(request, ("Login please"))
    
    return render(request, 'design/login.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'design/register.html', {'form': form})

def logout_view(request) :
    django_logout(request)
    messages.success(request, ("You have been logged out !!"))
    return redirect(index)


