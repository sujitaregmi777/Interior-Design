from django.shortcuts import render

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

# Create your views here.
