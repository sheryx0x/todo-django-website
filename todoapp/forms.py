from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import  UserCreationForm
from .models import *



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your task here'})