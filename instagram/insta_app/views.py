from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        print(f"Email: {email}, Password: {password}")

        user_obj = User.objects.get(email=email)
        user = authenticate(request, username=user_obj.username, password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password!")
            return redirect('login')
                
    else:
        return render(request, "login.html")
    
def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"] 
        password = request.POST["password"]


        if User.objects.filter(email=email).exists():
            messages.error(request, "This email address already exists")
            return redirect("signup")
            
        if User.objects.filter(username=username).exists():
            messages.error(request, "username aready exists")
            return redirect("signup")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successfull")
        return redirect('login')
    
    return render(request, "signup.html")

def home_page(request):
    return render(request, "home.html")

def user_logout(request):
    logout(request)
    return redirect("login")