from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class GuestForm(forms.Form):
    email = forms.EmailField()


class LoginForm(forms.Form):
    """docstring for ClassName"""
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    """docstring for ClassName"""
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label= "Confirm pasword")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.object.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data
