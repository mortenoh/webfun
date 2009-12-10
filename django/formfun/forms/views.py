
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import forms

class StudentForm(forms.Form):
	username = forms.CharField(max_length=64)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)

def index(request):
	form = StudentForm()
	return render_to_response("index.html", locals())

