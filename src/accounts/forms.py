from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Email Address'
                             }))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Password',
                               }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not 'gmail.com' in email:
            raise forms.ValidationError('Please enter correct email')
        return email


class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Email Address'
                             }))
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username',
                               }))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Password',
                               }))
    password2 = forms.CharField(label='Confirm-Password',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password',
                                }))

    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        qs = User.objects.filter(email=email)

        if not 'gmail.com' in email:
            if qs.exists():
                raise forms.ValidationError('Check email address')
            raise forms.ValidationError('Email already exists')

        password1 = data.get('password')
        password2 = data.get('password2')
        if password2 != password1:
            raise forms.ValidationError('Passwords miss match')
        return data
