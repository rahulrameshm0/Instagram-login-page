from django import forms
from . models import Login,SignUp

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ("Email","Password")

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ("Email","Password")

