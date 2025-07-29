from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('features/', features, name='features'), 
    path('work/', work, name='work'),
    path('contact/', contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='design/login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view , name='logout')


]
