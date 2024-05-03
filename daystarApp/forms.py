from django.forms import ModelForm
from .models import *
from django.forms import forms


class Signin(ModelForm):
    class Meta:
        model = Sign_in
        fields = '__all__'

class Signup(ModelForm):
    class Meta:
        model = Sign_up
        fields = '__all__'

class Addbaby(ModelForm):
    class Meta:
        model = Baby
        fields = '__all__'


#Babies
class Baby_doll(ModelForm):
    class Meta:
        model = Doll
        fields = '__all__' 

class Arrival_Form(ModelForm):
    class Meta:
        model = Arrival
        fields = '__all__'

class Departure_Form(ModelForm):  
    class Meta:
        model = Departure
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
        model =                         


