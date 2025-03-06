from django.shortcuts import render, redirect
from django.contrib.auth import aauthenticate
from django.contrib import messages
from . models import Login
from . forms import LoginForm, SignUpForm
# Create your views here.

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = aauthenticate(request, Email=email, Password=password)
            if user is not None:
                login(request,user)
                return redirect("main_page")
            else:
                form.add_error(None, "Invalid email or password!")
                
    else:
        form = LoginForm()
        login_users = Login.objects.all()
        return render(request, "login.html", {'form': form, 'login_users':login_users})
    
def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success("Account created successfully!")
            return redirect("login")
        # else:
    return render(request, "signup.html", {"form":form})

def main_page(request):
    pass