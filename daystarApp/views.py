from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models import Sum


# Create your views here.
def index(request):
    return render(request, 'daystarApp/index.html')
def about_us(request):
    return render(request, 'daystarApp/about_us.html')


# Sitters

def sit_add(request):
    if request.method == 'POST':
        form = Sitter_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sit_reg_form')
    else:
        form = Sitter_Form()
    return render(request, 'daystarApp/sit_add.html', {'form': form })


def sit_view(request, id):
    one_sitter = Sitterform.objects.get(id=id)
    return render(request, 'daystarApp/sit_view.html',{'one_sitter': one_sitter})

def sit_edit(request, id):
    sitter = get_object_or_404(Sitterform, id=id)
    if request.method == 'POST':
        form = Sitter_Form(request.POST, instance=sitter)
        if form.is_valid():
            form.save()
            return redirect('sit_reg_form')
    else:
        form = Sitter_Form(instance=sitter)
    return render(request, 'daystarApp/sit_edit.html', {'form': form, 'sitter': sitter})

def sit_reg_form(request):
    sit_form = Sitterform.objects.all()
    return render(request, 'daystarApp/sit_reg_form.html', {'sit_form': sit_form})

def sit_payments(request):
    return render(request, 'daystarApp/sit_payments.html')
def sit_arrival(request):
    return render(request, 'daystarApp/sit_arrival.html')
def sit_depart(request):
    return render(request, 'daystarApp/sit_depart.html')



# procurement 
    
def dolls(request):
    return render(request, 'daystarApp/dolls.html')

def stock(request):
    return render(request, 'daystarApp/stock.html')

   

    
  

    


# Babies

def baby_pay(request):
    return render(request, 'daystarApp/baby_pay.html')

def baby_depart(request):
    return render(request, 'daystarApp/baby_depart.html')

def baby_arrival(request):
    return render(request, 'daystarApp/baby_arrival.html')
def beb_reg_form(request):
    return render(request, 'daystarApp/beb_reg_form.html')

    
        

# authentication
def sign_in(request):
    signinform =None
    user = None
    if request.method == 'POST':
        signinform = Signin(request.POST)
        if signinform.is_valid():
            print('form is valid')
            email = signinform.cleaned_data['email']
            password = signinform.cleaned_data['password']
            user = authenticate(email=email, password=password)
            return redirect('index')
        else:
            signinform = Signin()

    else:
        signinform = Signin()
    return render(request, 'daystarApp/sign_in.html', {'signinform': signinform, 'user': user})

def sign_up(request):
    form =None
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
        else:
            form = Signup()
    return render(request, 'daystarApp/sign_up.html', {'form': form})

def forgot_pass(request):
    return render(request, 'daystarApp/forgot_pass.html')

def reset_pass(request):
    return render(request, 'daystarApp/reset_pass.html')

def new_pass(request):
    return render(request, 'daystarApp/new_pass.html')

