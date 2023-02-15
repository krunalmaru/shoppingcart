from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy,gettext as _



class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form-control'}),
    )
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "autofocus": True,'class':'form-control'}))
    new_password1 = forms.CharField(label=_(" New Password"),widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "autofocus": True,'class':'form-control'}),strip=False,help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_(" New Password (again)"),widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),strip=False,help_text=_("Enter the same password as before, for verification."))
