from django.shortcuts import render
from .models import Account
from .forms import SignupForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def valid(email):
  return not Account.objects.filter(email=email).exists()
def signup(request):
        
        if request.method == 'POST':
            #  username = request.POST.get('username')
            #  password = request.POST.get('password')
             email=request.POST.get('email')
      
             form = SignupForm(request.POST)
             if form.is_valid() and valid(email):
               user = form.save(commit=False)
               user.set_password(user.password)  
               user.save()
               return redirect('login')
    
            #  elif not valid(email):
            #     messages.error(request, "This email already exists")
                
        else:
            form = SignupForm()
        return render(request,'account/signup.html',{'form': form})

def loginv(request):
    if request.method == 'POST':
            password = request.POST.get('password')
            email=request.POST.get('email')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user) 
                print("USER:", user)
                return redirect('/dashboard/')
            else:
               print("USER:", user)
               messages.error(request, "Invalid email or password.")
    return render(request,'account/login.html')
def logoutv(request):
    logout(request)
    return redirect('login')

def about(request):

     return render(request,'about.html')
