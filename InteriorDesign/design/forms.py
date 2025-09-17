from django import forms
from .models import Work

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

class BookForm(forms.Form) :
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    Design = forms.CheckboxSelectMultiple()
    others = forms.CharField(widget=forms.Textarea)
    refrences = forms.ImageField()
    cost = forms.CharField()
    date = forms.DateField()

class WorkForm(forms.ModelForm):
    class  Meta:
        model = Work
        fields = ['name', 'image', 'cost', 'story']