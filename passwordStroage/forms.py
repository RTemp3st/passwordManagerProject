from django import forms
from .models import User
from .models import UserPW

class registerationForm(forms.Form):
    username = forms.CharField(label="Your Username")
    email = forms.EmailField(label="Your Email")
    password1 = forms.CharField(label="Your Password")
    password2 = forms.CharField(label="Your Password")

    def checkPassword(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("Please confirm your password.")
        if password1 != password2:
            raise forms.ValidationError("Your Password does not match.")
        return password1

    def checkUsername(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username_iexact=username)
        if qs.exists():
            raise forms.ValidationError("This username is already used, please use another username.")
        return username

    def checkEmail(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email_iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already used, please use another email.")
        return email

class loginForm(forms.Form):
    username = forms.CharField(label="Your Username")
    password = forms.CharField(label="Your Password")
