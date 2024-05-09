from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from . forms import *
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib import messages
from . filters import *
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models import Sum
from datetime import datetime



# Create your views here.


def index(request):
    return render(request, 'daystarApp/index.html')
def about_us(request):
    return render(request, 'daystarApp/about_us.html')


# Sitters

#sitters registration

def sit_reg_form(request):
    sit_form = Sitterform.objects.all().order_by('-id')
    all_sitters = SitterFilter(request.GET, queryset=sit_form)
    sit_form  = all_sitters.qs 
    return render(request, 'daystarApp/sit_reg_form.html', {'sit_form': sit_form, 'all_sitters': all_sitters})


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



#sitter arrivals
def sit_arrival(request):
    sit_arrive = Sitter_arrival.objects.all()
    return render(request, 'daystarApp/sit_arrival.html', {'sit_arrive': sit_arrive})


def sit_adds(request):
    if request.method == 'POST':
        form = Sitter_arrival_Form(request. POST)
        if form.is_valid():
            form.save()
            return redirect('sit_arrival')
    else:
        form = Sitter_arrival_Form()    
    return render(request, 'daystarApp/sit_adds.html', {'form': form})

def sit_views(request, id):
    sit_info = Sitter_arrival.objects.get(id=id) 
    return render(request, 'daystarApp/sit_views.html', {'sit_info': sit_info})

def sit_edits(request, id):
    edit = get_object_or_404(Sitter_arrival, id=id)
    if request.method == 'POST':
        form = Sitter_arrival_Form(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('sit_arrival')
    else:
        form = Sitter_arrival_Form(instance=edit)

    return render(request, 'daystarApp/sit_edits.html', {'form': form, 'edit': edit})


#sitter departure
def sit_depart(request):
    sit_leave = Sitter_departure.objects.all()
    return render(request, 'daystarApp/sit_depart.html', {'sit_leave': sit_leave})
   

def depart_view(request, id):
    view = Sitter_departure.objects.get(id=id)
    return render(request, 'daystarApp/depart_view.html', {'view': view})

    
def depart_add(request):
    if request.method == 'POST':
        form = Sitter_departure_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sit_depart')
    else:
        form = Sitter_departure_Form()    
    return render(request, 'daystarApp/depart_add.html', {'form': form})

def depart_edit(request, id):
    depart = get_object_or_404(Sitter_departure, id=id )
    if request.method == 'POST':
        form = Sitter_departure_Form(request.POST, instance=depart)
        if form.is_valid():
            form.save()
            return redirect('sit_depart')
    else:
        form = Sitter_departure_Form(instance=depart)    
    return render(request, 'daystarApp/depart_edit.html', {'form': form, 'depart': depart})


def sit_payments(request):
    sit_payment = Sitter_payment.objects.all()
    return render(request, 'daystarApp/sit_payments.html', {'sit_payment': sit_payment})

def add_sit_payment(request):
    if request.method == 'POST':
        form = Sitter_payment_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sit_payments')
    else:
        form = Sitter_payment_Form()
    return render(request, 'daystarApp/add_sit_payment.html', {'form': form})




   

    
# Babies

#baby registration

def beb_reg_form(request):
    baby_form = Baby.objects.all()
    return render(request, 'daystarApp/beb_reg_form.html', {'baby_form': baby_form})

def baby_add(request):
    if request.method == 'POST':
        form = Baby_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beb_reg_form')
    else:
        form = Baby_Form()
    return render(request, 'daystarApp/baby_add.html', {'form': form})

def baby_edit(request, id):
    baby = get_object_or_404(Baby, baby_id=id)
    if request.method == 'POST':
        form = Baby_Form(request.POST, instance=baby)
        if form.is_valid():
            form.save()
            return redirect('beb_reg_form')
    else:
        form = Baby_Form(instance=baby)
    return render(request, 'daystarApp/baby_edit.html', {'form': form, 'baby': baby})


def baby_view(request, id):
    one_baby = get_object_or_404(Baby, baby_id=id)
    return render(request, 'daystarApp/baby_view.html', {'one_baby': one_baby})





#baby departure
def baby_depart(request):
    baby_leave = BabyDeparture.objects.all()
    return render(request, 'daystarApp/baby_depart.html', {'baby_leave': baby_leave})

def depart_baby_add(request):
    if request.method == 'POST':
        form = Baby_departure_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baby_depart')
    else:
        form = Baby_departure_Form()    
    return render(request, 'daystarApp/depart_baby_add.html', {'form': form})
def depart_baby_view(request, baby_id):
    depart_info = BabyDeparture.objects.get(baby_id=baby_id)
    return render(request, 'daystarApp/depart_baby_view.html', {'depart_info': depart_info})

def depart_baby_edit(request, baby_id): 
    depart = get_object_or_404(BabyDeparture, baby_id=baby_id)
    if request.method == 'POST':

        form = Baby_departure_Form(request.POST, instance=depart)
        if form.is_valid():
            form.save()
            return redirect('baby_depart')
    else:
        form = Baby_departure_Form(instance=depart)    
    return render(request, 'daystarApp/depart_baby_edit.html', {'form': form, 'depart': depart})

   

#baby payment
def baby_pay(request):
    baby_payment = BabyPayment.objects.all()
    return render(request, 'daystarApp/baby_pay.html', {'baby_payment':baby_payment})

def add_baby_payment(request):
    if request.method == 'POST':
        form = Baby_payment_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baby_pay')
    else:
        form = Baby_payment_Form()    
    return render(request, 'daystarApp/add_baby_payment.html', {'form': form})
   
        

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



# procurement 
    
def dolls(request):
    return render(request, 'daystarApp/dolls.html')

def stock(request):
    return render(request, 'daystarApp/stock.html')



#dashboard
 

def index(request):
    
    # count_dolls = Doll.objects.all()
    # count_stock = Stock.objects.all()
    count_babies = Baby.objects.all().count()
    count_sitters = Sitterform.objects.all().count()
    last_babies = Baby.objects.all()[:5]
    last_sitters = Sitterform.objects.all()[:5]
    
    context = {
        "count_babies": count_babies,
        "count_sitters": count_sitters,
        "last_babies": last_babies,
        "last_sitters": last_sitters,
        # "count_dolls": count_dolls,
        # "count_stock": count_stock,
    }
    template = loader.get_template('daystarApp/index.html')
    return HttpResponse(template.render(context))