from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User


class LoginForm(auth_forms.AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}), max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}), max_length=25)


class SignUp(auth_forms.UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}),
                               max_length=150)
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': "form-control"}), max_length=50)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control"}),
                                max_length=25)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': "form-control"}),
                                max_length=25)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class PasswordReset(auth_forms.PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}), max_length=254)


class PasswordChange(auth_forms.PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}), max_length=25)
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': "form-control"}),
                                    max_length=25)
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(
             attrs={'class': "form-control"}), max_length=25)
