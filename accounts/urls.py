from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^password_reset/$', views.PasswordReset.as_view(), name='password_reset'),
    url(r'^password_change/$', views.PasswordChange.as_view(), name='password_change')
]
