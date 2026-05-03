from django.shortcuts import render
from .models import Account
from .forms import SignupForm
from django.shortcuts import render, redirect
from django.contrib import messages

def valid(email):
  return not Account.objects.filter(email=email).exists()
def signup(request):
        
        if request.method == 'POST':
            #  username = request.POST.get('username')
            #  password = request.POST.get('password')
             email=request.POST.get('email')
      
             form = SignupForm(request.POST)
             if form.is_valid() and valid(email):
                   form.save()
                   messages.success(request, "Sign-up completed successfully")
                   return redirect('login')

             elif not valid(email):
                messages.error(request, "This email already exists")
                
        else:
            form = SignupForm()
        return render(request,'account/signup.html',{'form': form})

def login(request):
    if request.method == 'POST':
            password = request.POST.get('password')
            email=request.POST.get('email')
            if Account.objects.filter(email=email, password=password).exists():
                   messages.success(request, "login completed successfully")
                   return redirect('Home')
            else:
                messages.error(request, "Invalid email or password.")
    return render(request,'account/login.html')
def home(request):
     return render(request,'account/Home.html')
def about(request):
     return render(request,'about.html')