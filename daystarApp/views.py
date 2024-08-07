from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from . forms import *
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from . filters import *
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models import Sum
from datetime import datetime
from django.http import HttpResponseBadRequest
from .filters import BabyFilter
from .models import Baby


def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Pass request to the form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # User authentication failed, render the form with an error message
                return render(request, 'daystarApp/index.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = AuthenticationForm()  # For GET requests, create a new form instance
    
    # Render the form initially or when there are validation errors
    return render(request, 'daystarApp/index.html', {'form': form})



@login_required
def home(request):
    return render(request, 'daystarApp/home.html')

@login_required
def about_us(request):
    return render(request, 'daystarApp/about_us.html')

@login_required
def logout(request):
    logout(request)
    return redirect('index')
    


# Sitters

#sitters registration
@login_required
def sit_reg_form(request):
    sit_form = Sitterform.objects.all().order_by('id') 
    all_sitters = SitterFilter(request.GET, queryset=sit_form)
    sit_form  = all_sitters.qs 
    return render(request, 'daystarApp/sit_reg_form.html', {'sit_form': sit_form, 'all_sitters': all_sitters})

@login_required
def sit_add(request):
    if request.method == 'POST':
        form = Sitter_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sit_reg_form')
    else:
        form = Sitter_Form()
    return render(request, 'daystarApp/sit_add.html', {'form': form })

@login_required
def sit_view(request, id):
    one_sitter = Sitterform.objects.get(id=id)
    return render(request, 'daystarApp/sit_view.html',{'one_sitter': one_sitter})

@login_required
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
@login_required
def sit_arrival(request):
    sit_arrive = Sitter_arrival.objects.all()
    return render(request, 'daystarApp/sit_arrival.html', {'sit_arrive': sit_arrive})

@login_required
def sit_adds(request):
    if request.method == 'POST':
        form = Sitter_arrival_Form(request. POST)
        if form.is_valid():
            form.save()
            return redirect('sit_arrival')
    else:
        form = Sitter_arrival_Form()    
    return render(request, 'daystarApp/sit_adds.html', {'form': form})

@login_required
def sit_views(request, id):
    sit_info = Sitter_arrival.objects.get(id=id) 
    return render(request, 'daystarApp/sit_views.html', {'sit_info': sit_info})

@login_required
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
@login_required
def sit_depart(request):
    sit_leave = Sitter_departure.objects.all()
    return render(request, 'daystarApp/sit_depart.html', {'sit_leave': sit_leave})
   
@login_required
def depart_view(request, id):
    view = Sitter_departure.objects.get(id=id)
    return render(request, 'daystarApp/depart_view.html', {'view': view})

@login_required    
def depart_add(request):
    if request.method == 'POST':
        form = Sitter_departure_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sit_depart')
    else:
        form = Sitter_departure_Form()    
    return render(request, 'daystarApp/depart_add.html', {'form': form})


@login_required
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


@login_required
def sit_payments(request):
    sit_payment = Sitter_payment.objects.all()
    return render(request, 'daystarApp/sit_payments.html', {'sit_payment': sit_payment})

@login_required
def add_sit_payment(request):
    if request.method == 'POST':
        form = Sitter_payment_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sit_payments')
    else:
        form = Sitter_payment_Form()
    return render(request, 'daystarApp/add_sit_payment.html', {'form': form})


@login_required
def edit_sit_payment(request, id):
    edit = get_object_or_404(Sitter_payment, id=id)
    if request.method == 'POST':
        form = Sitter_payment_Form(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('sit_payments')
    else:
        form = Sitter_payment_Form(instance=edit)
    return render(request, 'daystarApp/edit_sit_payment.html', {'form': form, 'edit': edit})

   

    
# Babies

#baby registration
 
@login_required
def beb_reg_form(request):
    baby_form = Baby.objects.all().order_by('baby_id')
    all_babies = BabyFilter(request.GET, queryset=baby_form)
    baby_form  = all_babies.qs
    return render(request, 'daystarApp/beb_reg_form.html', {'baby_form': baby_form, 'all_babies': all_babies})

@login_required
def baby_add(request):
    if request.method == 'POST':
        form = Baby_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beb_reg_form')
    else:
        form = Baby_Form()
    return render(request, 'daystarApp/baby_add.html', {'form': form})

@login_required
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

@login_required
def baby_view(request, id):
    one_baby = get_object_or_404(Baby, baby_id=id)
    return render(request, 'daystarApp/baby_view.html', {'one_baby': one_baby})



#baby departure
@login_required
def baby_depart(request):
    baby_leave = BabyDeparture.objects.all()
    return render(request, 'daystarApp/baby_depart.html', {'baby_leave': baby_leave})

@login_required
def depart_baby_add(request):
    if request.method == 'POST':
        form = Baby_departure_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baby_depart')
    else:
        form = Baby_departure_Form()    
    return render(request, 'daystarApp/depart_baby_add.html', {'form': form})

@login_required
def depart_baby_view(request, baby_id):
    depart_info = BabyDeparture.objects.get(baby_id=baby_id)
    return render(request, 'daystarApp/depart_baby_view.html', {'depart_info': depart_info})


@login_required
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
@login_required
def baby_pay(request):
    baby_payment = BabyPayment.objects.all()
    return render(request, 'daystarApp/baby_pay.html', {'baby_payment':baby_payment})


@login_required
def add_baby_payment(request):
    if request.method == 'POST':
        form = Baby_payment_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baby_pay')
    else:
        form = Baby_payment_Form()    
    return render(request, 'daystarApp/add_baby_payment.html', {'form': form})

@login_required
def edit_baby_payment(request, id):
    baby_pay = get_object_or_404(BabyPayment, baby_id=id)
    if request.method == 'POST':
        form = Baby_payment_Form(request.POST, instance=baby_pay)
        if form.is_valid():
            form.save()
            return redirect('baby_pay')
    else:
        form = Baby_payment_Form(instance=baby_pay)
    return render(request, 'daystarApp/edit_baby_payment.html', {'form': form, 'baby_pay': baby_pay})

# Baby receipt



@login_required
def baby_receipt(request):
    babe_receipt = BabyPayment.objects.all().order_by('-baby_id')
    return render(request,'daystarApp/baby_receipt.html',{'babe_receipt':babe_receipt})

@login_required
def baby_receipt_detail(request, id):
    receipt_detail = BabyPayment.objects.get(baby_id=id)
    return render(request, 'daystarApp/baby_receipt_detail.html', {'receipt_detail': receipt_detail})




# procurement 
@login_required   
def doll_list(request):
    dolls_list = Doll.objects.all()
    return render(request, 'daystarApp/doll_list.html', {'dolls_list':dolls_list})

@login_required
def add_doll(request):
    if request.method == 'POST':
        form = Doll_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doll_list')
    else:
        form = Doll_Form()
    return render(request, 'daystarApp/add_doll.html', {'form': form})

@login_required
def doll_view(request, id):
    one_doll = get_object_or_404(Doll, doll_id=id)
    return render(request, 'daystarApp/doll_view.html', {'one_doll': one_doll})


@login_required
def doll_pay(request, id):
    sold_item = Doll.objects.get(pk=id)
    pay_form = Doll_payment_Form(request.POST)

    if request.method == 'POST':
        if pay_form.is_valid():
            new_payment = pay_form.save(commit=False)
            new_payment.name = sold_item
            new_payment.doll_price = sold_item.doll_price
            new_payment.save()
            sold_quantity = int(request.POST.get('doll_quantity'))
            sold_item.doll_quantity -= sold_quantity
            sold_item.save()
            print(sold_item.doll_name)
            print(request.POST['doll_quantity'])
            print(sold_item.doll_quantity)
            return redirect('doll_receipt')
        else:
            # Handle the case when the form is not valid
            return render(request, 'daystarApp/doll_pay.html', {'pay_form': pay_form})
    else:
        # Handle the case when the request method is not POST
        return render(request, 'daystarApp/doll_pay.html', {'pay_form': pay_form})

#Doll receipt

@login_required
def receipt_detail(request, id):
    #below is a query
    #querying data by id
    receipt = Doll_payment.objects.get(id=id)
    return render( request,'daystarApp/receipt_detail.html',{'receipt':receipt})


@login_required
def doll_receipt(request):
    dolls = Doll_payment.objects.all().order_by('-id')
    return render(request,'daystarApp/doll_receipt.html',{'dolls':dolls})


@login_required
def doll_pay_list(request):
    doll_payment = Doll_payment.objects.all()
    return render(request, 'daystarApp/doll_pay_list.html', {'doll_payment': doll_payment})

@login_required
def add_one_doll(request, id):
    added_doll = Doll.objects.get(doll_id=id)
    if request.method == 'POST':
        form = Add_doll(request.POST)
        if form.is_valid():
           old_doll = request.POST.get('doll_quantity')
           if old_doll:
              try:
                   new_doll = int(old_doll)
                   added_doll.doll_quantity += new_doll
                   added_doll.save()
                   print(new_doll)
                   print(added_doll.doll_quantity)
                   return redirect('doll_list')
              except ValueError:
                  return HttpResponseBadRequest('Invalid doll')
    else:
        form = Add_doll()
        return render(request, 'daystarApp/add_one_doll.html', {'form': form, 'added_doll': added_doll})                    


@login_required 
def doll_edit(request, id):
    edited_doll = get_object_or_404(Doll, doll_id=id)
    if request.method == 'POST':
         form = Doll_Form(request.POST, instance=edited_doll)
         if form.is_valid():
             form.save()
             return redirect('doll_list')
    else:
         form = Doll_Form(instance=edited_doll)
    return render(request, 'daystarApp/doll_edit.html', {'form': form, 'edited_doll': edited_doll})

     


@login_required
def stock_list(request):
    stock_list = Stock.objects.all()
    return render(request, 'daystarApp/stock_list.html', {'stock_list': stock_list})

@login_required
def add_stock(request):
    if request.method == 'POST':
        form = Stock_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = Stock_Form()    

    return render(request, 'daystarApp/add_stock.html', {'form': form})

@login_required
def stock_view(request, id):
    one_stock = get_object_or_404(Stock, stock_id=id)
    return render(request, 'daystarApp/stock_view.html', {'one_stock': one_stock})

@login_required    
def stock_edit(request, id):
    edited_stock = get_object_or_404(Stock, stock_id=id)
    if request.method == 'POST':
         form = Stock_Form(request.POST, instance=edited_stock)
         if form.is_valid():
             form.save()
             return redirect('stock_list')
    else:
         form = Stock_Form(instance=edited_stock)
    return render(request, 'daystarApp/stock_edit.html', {'form': form, 'edited_stock': edited_stock})     

@login_required
def add_one_stock(request, id):
    added_stock = Stock.objects.get(stock_id=id)
    if request.method == 'POST':
        form = Add_stock(request.POST)
        if form.is_valid():
           old_stock = request.POST.get('stock_quantity')
           if old_stock:
              try:
                   new_stock = int(old_stock)
                   added_stock.stock_quantity += new_stock
                   added_stock.save()
                   print(new_stock)
                   print(added_stock.stock_quantity)
                   return redirect('stock_list')
              except ValueError:
                  return HttpResponseBadRequest('Invalid stock')
    else:
        form = Add_stock()

        return render(request, 'daystarApp/add_one_stock.html', {'form':form , 'added_stock':added_stock})


@login_required
def stock_issue(request, id):
    issued_stock = Stock.objects.get(pk=id)
    issue_form = Stock_issueForm(request.POST)

    if request.method == 'POST':
        if  issue_form.is_valid():
            new_stock = issue_form.save(commit=False)
            new_stock.stock_name = issued_stock
            new_stock.stock_price = issued_stock.stock_price
            new_stock.save()
            issued_quantity = int(request.POST['stock_quantity'])
            issued_stock.stock_quantity -= issued_quantity
            issued_stock.save()
            print(issued_stock.stock_name)
            print(request.POST['stock_quantity'])
            print(issued_stock.stock_quantity)
            return redirect('stock_list')
    else:
       
      return render(request, 'daystarApp/stock_issue.html', {'issue_form': issue_form})



#dashboard
 
@login_required
def home(request):
    
    count_dolls = Doll.objects.all().count()
    count_stock = Stock.objects.all().count()
    count_babies = Baby.objects.all().count()
    count_sitters = Sitterform.objects.all().count()
    last_babies = Baby.objects.all()[:5]
    last_sitters = Sitterform.objects.all()[:5]
    
    context = {
        "count_babies": count_babies,
        "count_sitters": count_sitters,
        "last_babies": last_babies,
        "last_sitters": last_sitters,
        "count_dolls": count_dolls,
        "count_stock": count_stock,
    }
    template = loader.get_template('daystarApp/home.html')
    return HttpResponse(template.render(context))





# def forgot_pass(request):
#     return render(request, 'daystarApp/forgot_pass.html')

# def reset_pass(request):
#     return render(request, 'daystarApp/reset_pass.html')

# def new_pass(request):
#     return render(request, 'daystarApp/new_pass.html')

