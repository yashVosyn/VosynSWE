from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
# Create your views here.
def home(request):
    return render(request,"user/index.html")

def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        messages.success(request,"your account has been succesfully created.")
        
        return redirect("signin")
        
    return render(request,"user/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass1']
        
        
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"authentication/index.html",{'fname':fname})
            
        else:
            messages.error(request,'Bad Credentials')
            return redirect('home')            
            
    return render(request,"user/signin.html")
def signout(request):
    pass
        