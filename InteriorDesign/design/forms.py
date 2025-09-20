from django import forms
from .models import Work

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

class BookForm(forms.Form) :
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    design = forms.CharField(max_length=255)
    other = forms.CharField(widget=forms.Textarea)
    references = forms.ImageField(required=False)
    cost = forms.IntegerField()
    date  = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class WorkForm(forms.ModelForm):
    class  Meta:
        model = Work
        fields = ['name', 'image', 'cost', 'story']