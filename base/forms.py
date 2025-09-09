from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'body', 'author']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }