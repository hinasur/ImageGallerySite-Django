from django import forms

from .models import PhotoImage,Review

class PhotoImageForm(forms.ModelForm):

  class Meta:
    model = PhotoImage
    fields = ('author','title', 'link', 'image')

class ReviewForm(forms.ModelForm):

  class Meta:
    model = Review
    fields = ('author', 'title', 'content')
