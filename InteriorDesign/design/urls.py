from django.urls import path
from . views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('features/', features, name='features'), 
    path('work/', work, name='work'),
    path('contact/', contact, name='contact'),
]
