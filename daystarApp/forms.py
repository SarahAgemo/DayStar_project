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

class Baby_Payment(ModelForm):
    class Meta:
        model = BabyPayment
        fields = '__all__'

class Baby_doll(ModelForm):
    class Meta:
        model = Doll
        fields = '__all__'        

