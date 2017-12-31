from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView

from . import forms


class Login(LoginView):
    template_name = 'registration/login.html'
    form_class = forms.LoginForm


class SignUp(generic.CreateView):
    template_name = 'signup.html'
    form_class = forms.SignUp
    success_url = reverse_lazy('login')


class PasswordReset(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    form_class = forms.PasswordReset
    success_url = reverse_lazy('password_reset_done')


class PasswordChange(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    form_class = forms.PasswordChange
    success_url = reverse_lazy('password_change_done')
