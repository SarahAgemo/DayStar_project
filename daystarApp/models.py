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
class Sign_in(models.Model):
     email = models.EmailField(max_length=30, blank=True, null=True)
     password = models.CharField(max_length=20, blank=True, null=True)

     def __str__(self):
         return self.email

class Sign_up(models.Model):
    name = models.CharField( max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    phone = models.IntegerField( null=True, blank=True)
    password = models.CharField( max_length=20, blank=True, null=True)
    repeat_password = models.CharField( max_length=20, blank=True, null=True)
   
    def __str__(self):
        return self.name

class Forgot_pass(models.Model):
    email = models.EmailField(max_length=30, blank=True, null=True)
   

    def __str__(self):
        return self.email
    
class Reset_pass(models.Model):
    otp = models.IntegerField(null=True, blank=True)    
    
    def __int__(self):
        return self.otp
    
class New_pass(models.Model):
    new_password = models.CharField(max_length=20, blank=True, null=True)
    confirm_password = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.confirm_password
    
   

#sitters
class Sitterform(models.Model):  
    name=models.CharField(max_length=200)
    gender=models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=100)
    location=models.CharField(choices=[('kabalagala', 'kabalagala')], max_length=100)
    date_of_birth=models.DateField(default=timezone.now) 
    next_of_kin=models.CharField( max_length=200)
    national_identification_number=models.CharField(max_length=200, validators=[NIN])
    recommenders_name=models.CharField(max_length=200)
    religon=models.CharField(max_length=200,null=True, blank=True)
    level_of_education=models.CharField( choices=[('degree','Degree'),('diploma','Diploma'),('highschool certificate','Highschool certificate'),('others','Others')],max_length=200)
    sitter_number=models.IntegerField(default=0)
    contacts=models.CharField(max_length=200, validators=[contacts]) 
    date=models.DateField()
    def __str__(self):
        return self.name

class Sitter_arrival(models.Model):
    sitter_name=models.ForeignKey(Sitterform, on_delete=models.CASCADE) 
    sitter_number=models.IntegerField(default=0)
    date_of_arrival=models.DateField(default=timezone.now)   
    timein=models.TimeField ()
    Attendancestatus=models.CharField(choices=[('On-duty', 'On-duty')], max_length=100)
    def __str__(self):
        return str(self.sitter_name)
    
class Sitter_departure(models.Model):
    sitter_name=models.ForeignKey(Sitter_arrival, on_delete=models.CASCADE) 
    sitter_number=models.IntegerField(default=0)
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
    doll_type = models.CharField( max_length=20, blank=True, null=True)
    doll_name = models.CharField( max_length=20, blank=True, null=True)
    doll_price = models.IntegerField( null=True, blank=True, default=0)
    doll_description = models.TextField( max_length=30, blank=True, null=True)
    doll_image = models.ImageField(upload_to='doll_images', blank=True, null=True)

    def __str__(self):
        return self.doll_name
    
class Doll_payment(models.Model):
    doll_type = models.CharField( max_length=20, blank=True, null=True )
    name = models.ForeignKey(Doll, on_delete=models.CASCADE)
    amount_paid = models.IntegerField(default=0)
    doll_price = models.IntegerField( null=True, blank=True, default=0)    
    

    def __str__(self):
        return f"{self.name.doll_name} Payment"