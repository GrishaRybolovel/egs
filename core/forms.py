from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control form-control-user'}), max_length=100)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                          'class': 'form-control form-control-user'}), max_length=100)
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password',
                                                              'class': 'form-control form-control-user'}), max_length=100)
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Repeat Password',
                                                              'class': 'form-control form-control-user'}), max_length=100)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']