from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.


# Home page
def home_page(request):
    # return HttpResponse("welcome to the Home page")
    return render(request, "homepage.html")

# registration view function 
def sign_up(request):
    if request.method == "POST":
        frm = SignUpForm(request.POST)
        if frm.is_valid():
            frm.save()
            messages.success(request, "Account Created Sucessfully !! ")
            return HttpResponseRedirect('/login/')
    else:
        frm = SignUpForm()
    return render(request, "signup.html", {'form' : frm})
    
# login view function
def userlogin(request):
    #import pdb;pdb.set_trace()
    if request.method == 'POST':
        frm = AuthenticationForm(request=request, data = request.POST)
        if frm.is_valid():
            usname = frm.cleaned_data['username']
            uspass = frm.cleaned_data['password']
            userobj = authenticate(username = usname , password = uspass)
            if userobj is not None:
                login(request, userobj)
                messages.success(request, "Login Sucessfully !!")
                return HttpResponseRedirect('/profile/')
    else: # (if method is get then it comes to else part)
        frm = AuthenticationForm()
        # messages.success(request, "Please enter your credentials")
        # return HttpResponseRedirect('/userlogin/')
    return render(request, "userlogin.html", {'form' : frm})

# profile view function 
def user_profile(request):
    return render(request, 'profile.html')


# logout function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')