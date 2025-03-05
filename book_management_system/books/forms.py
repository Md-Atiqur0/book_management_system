from .models  import Books
from django import forms

class BookForms(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title','author','description','published_year']
