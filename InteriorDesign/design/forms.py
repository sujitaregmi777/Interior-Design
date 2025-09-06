from django import forms

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
    
