
from django import forms

class BlogForm(forms.Form):
	author = forms.CharField(max_length=32)
	subject = forms.CharField(max_length=128)
	body = forms.SlugField(widget=forms.Textarea)

