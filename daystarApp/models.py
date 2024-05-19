from django.db import models
from django.utils import timezone
import re
from django.core.exceptions import ValidationError



# Create your models here.
 

def contacts(value):
    if len(value) !=10:
        raise ValidationError("Only 10 digits are allowed")

def NIN(value):
    if len(value) !=14:
        raise ValidationError("Only 14 digits are allowed")           




   # Authentication 




   

#sitters
class Sitterform(models.Model):  
    name=models.CharField(max_length=200)
    gender=models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=100)
    location=models.CharField(choices=[('kabalagala', 'kabalagala')], max_length=100)
    date_of_birth=models.DateField(default=timezone.now) 
    next_of_kin=models.CharField( max_length=200)
    national_identification_number=models.CharField(max_length=200, validators=[NIN])
    recommenders_name=models.CharField(max_length=200)
    religion=models.CharField(max_length=200)
    level_of_education=models.CharField( choices=[('degree','Degree'),('diploma','Diploma'),('highschool certificate','Highschool certificate'),('others','Others')],max_length=200)
    
    contacts=models.CharField(max_length=200, validators=[contacts]) 
    date=models.DateField()
    def __str__(self):
        return self.name

class Sitter_arrival(models.Model):
    sitter_name=models.ForeignKey(Sitterform, on_delete=models.CASCADE) 
   
    date_of_arrival=models.DateField(default=timezone.now)   
    timein=models.TimeField ()
    Attendancestatus=models.CharField(choices=[('On-duty', 'On-duty')], max_length=100)
    def __str__(self):
        return str(self.sitter_name)
    
class Sitter_departure(models.Model):
    sitter_name=models.ForeignKey(Sitter_arrival, on_delete=models.CASCADE) 
   
    date_of_departure=models.DateField(default=timezone.now)   
    timeout=models.TimeField ()
    Attendancestatus=models.CharField(choices=[('offduty', 'offduty')], max_length=100)

    def __str__(self):
        return str(self.sitter_name)    


 # Babies
class Baby(models.Model):
    baby_id = models.AutoField(primary_key=True)
    baby_name = models.CharField( max_length=20)
    baby_gender = models.CharField( max_length=20 )
    date_of_birth = models.DateField( default=timezone.now)
    baby_location = models.CharField( max_length=20)
    # baby_image = models.ImageField(upload_to='baby_images', blank=True, null=True)
    parents_name = models.CharField( max_length=20)
    period_of_stay = models.CharField(choices=[('half-day', 'Half-day'),('full-day', 'Full-day')], max_length=100)
    registration_date = models.DateField(default=timezone.now)
    baby_bringer = models.CharField( max_length=20)
    time_in = models.TimeField()
    Assigned_to=models.ForeignKey(Sitter_arrival,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.baby_name


class BabyPayment(models.Model):
    baby_id = models.AutoField(primary_key=True)
    name_of_baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    period_of_stay = models.CharField(choices=[('half-day', 'Half-day'),('full-day', 'Full-day'),('monthly-halfday','Monthly-halfday'),('monthly-fullday','Monthly-fullday')], max_length=100)
    amount_paid = models.IntegerField(default=0)
    original_amount = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
    parent_name = models.CharField(max_length=20)
    amount_due = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name_of_baby.baby_name} Payment"

    def baby_payment(self): 
        b_payment = self.original_amount - self.amount_paid
        return int(b_payment)   



class BabyDeparture(models.Model):
    baby_id = models.AutoField(primary_key=True)
    name_of_baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    baby_picker = models.CharField( max_length=20)
    date_of_departure = models.DateField(default=timezone.now)
    time_out = models.TimeField()
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name_of_baby.baby_name} Departure" 
    
#sitter payment    
class Sitter_payment(models.Model): 
    sitter_name=models.ForeignKey(Sitter_arrival, on_delete=models.CASCADE) 
    amount=models.IntegerField(default=3000)
    date=models.DateField(default=timezone.now)
    no_of_babies=models.IntegerField(default=0)
    def __str__(self):
        return str(self.sitter_name)

    def total_payment(self):
        payment = self.no_of_babies * self.amount
        return int(payment)     


# dolls
class Doll(models.Model):
    doll_id = models.AutoField(primary_key=True)
    doll_type = models.CharField(choices=[('birds', 'Birds'),('animals', 'Animals'),('vehicles','Vehicles'),('human','Human'),('other','Other')], max_length=20)
    doll_name = models.CharField( max_length=20)
    doll_price = models.IntegerField( null=True, blank=True, default=0)
    doll_description = models.TextField( max_length=30, blank=True, null=True)
    doll_quantity = models.IntegerField( null=True, blank=True, default=0)
    # doll_image = models.ImageField(upload_to='doll_images', blank=True, null=True)

    def __str__(self):
        return self.doll_name
    
class Doll_payment(models.Model):
    babe_name = models.ForeignKey(Baby, on_delete=models.CASCADE)
    doll_type = models.CharField(choices=[('birds', 'Birds'),('animals', 'Animals'),('vehicles','Vehicles'),('human','Human'),('other','Other')], max_length=20)
    name = models.ForeignKey(Doll, on_delete=models.CASCADE)
    amount_paid = models.IntegerField(default=0)
    doll_price = models.IntegerField( null=True, blank=True, default=0)
    doll_quantity = models.IntegerField( null=True, blank=True, default=0) 
    parents_name = models.CharField( max_length=20)
    date = models.DateField(default=timezone.now)
    amount_due = models.IntegerField(default=0)

    

    def __str__(self):
        return f"{self.name.doll_name} Payment"
    
    def doll_payment(self): 
        d_payment = self.doll_price - self.amount_paid
        return int(d_payment)
    

class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    stock_type = models.CharField(choices=[('milk', 'Milk'),('diapers', 'Diapers'),('fruits', 'Fruits'),('wipes','Wipes'),('other','Other')], max_length=200)    
    stock_name = models.CharField(max_length=200)
    stock_price = models.IntegerField(default=0)
    stock_quantity = models.IntegerField(default=0)
    stock_description = models.TextField( max_length=30, blank=True, null=True)
    date_stocked = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.stock_name
    
class Stock_issue(models.Model):
    stock_type = models.CharField(choices=[('milk', 'Milk'),('diapers', 'Diapers'),('fruits', 'Fruits'),('wipes','Wipes')], max_length=200)    
    name = models.ForeignKey(Stock, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name.stock_name} Issue" 
