from django import forms

class PhotoForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'cutom-file-input'}))