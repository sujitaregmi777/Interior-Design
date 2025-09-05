from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

class BookForm(forms.Form) :
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    Design = forms.CharField(widget=forms.Textarea)
    # color = forms.color
    others = forms.CharField(widget=forms.Textarea)
    refrences = forms.ImageField()
    date = forms.DateField()
    
