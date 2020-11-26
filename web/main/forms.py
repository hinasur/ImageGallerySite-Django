from django import forms

from .models import PhotoImage

class PhotoImageForm(forms.ModelForm):

  class Meta:
    model = PhotoImage
    fields = ('author','title', 'link', 'image')