from django.shortcuts import render, redirect 
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'daystarApp/index.html')
def about_us(request):
    return render(request, 'daystarApp/about_us.html')

# Sitters


def sit_reg_form(request):
    return render(request, 'daystarApp/sit_reg_form.html')
def sit_payments(request):
    return render(request, 'daystarApp/sit_payments.html')
def sit_comments(request):
    return render(request, 'daystarApp/sit_comments.html')
def sit_attend(request):
    return render(request, 'daystarApp/sit_attend.html')
def sit_ass_babes(request):
    return render(request, 'daystarApp/sit_ass_babes.html')
def view_sit(request):
    return render(request, 'daystarApp/view_sit.html')

# procurement / dolls
# def doll_list(request):
#    
def pro_dolls(request):
    if request.method == 'POST':
        baby_dolls =  Baby_doll(request.POST)
        if baby_dolls.is_valid():
            baby_dolls.save()
            return redirect('baby_list')
    else:
        baby_dolls =  Baby_doll()

    context = {'baby_dolls': baby_dolls}
    return render(request, 'daystarApp/pro_dolls.html', context)

# def add_to_dolls(request , doll_id):
   
    
 

   

# def remove_from_dolls(request, doll_id):
#    

    
  

    


# Babies

def add_baby(request):
    if request.method == 'POST':
        baby_form = Addbaby(request.POST)
        if baby_form.is_valid():
            baby_form.save()
            return redirect('baby_list')
    else:
        baby_form = Addbaby()

    context = {'baby_form': baby_form}
    return render(request, "daystarApp/add_baby.html", context)     

def baby_list(request):
    result_count = 0
    if request.method == "POST":
        query = request.POST.get['query']
        all_babies = Baby.objects.filter(name_contains=query)
    else:
        all_babies = Baby.objects.all()[:5]
    result_count = len(all_babies)
    context = {
        'all_babies': all_babies,
       'result_count': result_count,
    }
    template = loader.get_template("daystarApp/baby_list.html")
    return HttpResponse(template.render(context))


def view_bebs(request, baby_id):
    baby_obj = Baby.objects.get(baby_id=baby_id)  # Assuming you have a Baby model
    all_payments = BabyPayment.objects.filter(baby=baby_obj)  # Use the correct manager and filter criteria
    enrollments = Registered_baby.objects.filter(baby=baby_obj)  # Assuming you have a Registered_baby model
    context = {
        "baby": baby_obj,
        "all_payments": all_payments,
        "enrollments": enrollments,
    }
    template = loader.get_template("daystarApp/view_bebs.html")
    return HttpResponse(template.render(context))

def baby_pay(request):
    if request.method == 'POST':
        baby_payments = Baby_Payment(request.POST)
        if baby_payments.is_valid():
            baby_payments.save()
            return redirect('index')
    else:
        baby_payments = Baby_Payment()

    context = {'baby_payments': baby_payments}
    return render(request, 'daystarApp/baby_pay.html', context)

def baby_comments(request):
    return render(request, 'daystarApp/baby_comments.html')

def baby_attend(request):
    return render(request, 'daystarApp/baby_attend.html')
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

