from django import forms
#from .models import *
from django.contrib.auth.models import User
from django.core import validators
#from  django.core.validators import validate_email

class LoginForm(forms.Form):
     username=forms.CharField()
     password=forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
     first_name=forms.CharField()
     last_name=forms.CharField()
     email=forms.EmailField()
     username=forms.CharField()
     password=forms.CharField(widget=forms.PasswordInput)
     password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
     def clean_username(self):
          username=self.cleaned_data.get('username')
          qs=User.objects.filter(username=username)
          
          if qs.exists():
               raise forms.ValidationError("Username already exist")
          return username

     def clean_email(self):
          email=self.cleaned_data.get('email')
          qs=User.objects.filter(email=email)
          if qs.exists():
               raise forms.ValidationError("Email already exist")
          return email

     def clean(self):
          data=self.cleaned_data
          password=self.cleaned_data.get("password")
          password2=self.cleaned_data.get("password2")
          if password2!=password:
               raise forms.ValidationError("Password must match")
          return data
          


class signForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}), required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={
                            'class': 'form-control', 'placeholder': 'Email address'}), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Create password'}), required=True, max_length=50)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm password'}), required=True, max_length=50)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        a = User.objects.filter(username=username)

        if a.exists():
            raise forms.ValidationError("Username already exist")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        a = User.objects.filter(email=email)
        if a.exists():
            raise forms.ValidationError("Email already exist")
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        MIN_LENGTH = 8
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Password does't match")
            else:
                if len(password) < MIN_LENGTH:
                    raise forms.ValidationError(
                        "Password should have atleast %d characters" % MIN_LENGTH)
                if password.isdigit():
                    raise forms.ValidationError(
                        "Password should not all numeric")

    class Meta():
        model = User
        fields = ['username', 'email', 'password']


