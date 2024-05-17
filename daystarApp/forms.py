from django.forms import ModelForm
from .models import *
from django.forms import forms
from django import forms





#Babies
class Baby_doll(ModelForm):
    class Meta:
        model = Doll
        fields = '__all__' 

class Baby_Form(ModelForm):
    class Meta:
        model = Baby
        fields = '__all__'        

class Baby_departure_Form(ModelForm):  
    class Meta:
        model = BabyDeparture
        fields = '__all__'      

class Baby_payment_Form(ModelForm):
    class Meta:
        model = BabyPayment
        fields = '__all__'        

# sitters

class Sitter_Form(ModelForm):
    class Meta:
        model = Sitterform
        fields = '__all__'

class Sitter_arrival_Form(ModelForm):
    class Meta:
        model = Sitter_arrival
        fields = '__all__'

class Sitter_departure_Form(ModelForm):
    class Meta:
        model = Sitter_departure
        fields = '__all__'

class Sitter_payment_Form(ModelForm):
    class Meta:
        model = Sitter_payment
        fields = '__all__'
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.fields['amount'].disabled = True



#dolls

class Doll_Form(ModelForm):
    class Meta:
        model = Doll
        fields = '__all__'

class Doll_payment_Form(ModelForm):
    class Meta:
        model = Doll_payment
        fields = '__all__'

    
class Add_doll(ModelForm):
    class Meta:
        model = Doll
        fields = ['doll_quantity']

#Stock

class Stock_Form(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

class Add_stock(ModelForm): 
    class Meta:
        model = Stock
        fields = ['stock_quantity']  

class Stock_issueForm(ModelForm):
    class Meta:
        model = Stock_issue
        fields = '__all__'



