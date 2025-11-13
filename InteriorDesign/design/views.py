from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as django_logout
from .forms import ContactForm , BookForm ,WorkForm
from .forms import Work 
from django.core.mail import EmailMessage


def index(request):
    works = Work.objects.all() 
    form = ContactForm()
    context = {
        'works': works,
        
        
    }
    return render(request, 'design/index.html', context)

@login_required
def book(request):
    context = {}
    
    if request.method == 'POST':
        form = BookForm(request.POST , request.FILES)
        
        if form.is_valid():
            try:
                name = request.POST.get('name')
                email = request.POST.get('email')
                design = request.POST.get('design')
                other = request.POST.get('other')
                references = request.FILES.get('references')
                cost = request.POST.get('cost')
                date = request.POST.get('date')
                message=f"Email: {email}\n\nDesign:\n{design}\n\nOther : {other}\n\nCost :{cost}\n\nDate: {date}"

                if references:
                    message += f"\nReferences file name: {references.name}"
                
                else:
                    message += "References: (not provided)"


                email_message = EmailMessage(
                    subject=f"Book Form Submission from {name}",
                    body= message, 
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                )

                if references:
                    email_message.attach(references.name, references.read(), references.content_type)

                    email_message.send(fail_silently=False)

                context['result'] = 'Email sent successfully'

            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'

    else:
        form = BookForm()

        design = request.GET.get('design')
        cost = request.GET.get('cost')
        image = request.GET.get('image')

        if design:
            form.fields['design'].initial = design
        if cost:
            form.fields['cost'].initial = cost
        if image:
            context['image'] = image



    context['form'] = form

    return render(request, 'design/book.html' , context)

@login_required
def explore(request):
    if request.method == "POST":
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('work')  
    else:
        form = WorkForm()
    return render(request, 'design/explore.html' , {'form' : form})

@login_required
def work(request):
    works = Work.objects.all()   
    return render(request, 'design/work.html', {'works': works})

@login_required(login_url='login')
def contact(request):
    context = {}
    form = ContactForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')

        if name and email and content:
            try:
                EmailMessage(
                    subject=f"Contact Form Submission from {name}",
                    message=f"Email: {email}\n\nMessage:\n{content}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )



                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    context['form'] = form

    return render(request, 'design/contact.html', context)

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


