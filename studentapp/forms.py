from core.models import Student
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# class LoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput)
#     password = forms.CharField(widget=forms.PasswordInput)
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'Registrations_No', 'Branch', 'phone', 'semester']
