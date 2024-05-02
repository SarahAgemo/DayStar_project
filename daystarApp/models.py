from django.db import models
from django.utils import timezone


# Create your models here.

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
    
    # Babies

class Baby(models.Model):
    baby_id = models.AutoField(primary_key=True)
    baby_name = models.CharField( max_length=20, blank=True, null=True)
    baby_gender = models.CharField( max_length=20, blank=True, null=True)
    baby_age = models.IntegerField( null=True, blank=True)
    baby_location = models.CharField( max_length=20, blank=True, null=True)
    # baby_image = models.ImageField(upload_to='baby_images', blank=True, null=True)
    baby_bringer = models.CharField( max_length=20, blank=True, null=True)
    baby_arrivaltime = models.DateTimeField( null=True, blank=True)
    parents_name = models.CharField( max_length=20, blank=True)
    period_of_stay = models.CharField( null=True, blank=True, max_length=10)
   

    def __str__(self):
        return self.baby_name

# dolls
class Doll(models.Model):
    doll_type = models.CharField( max_length=20, blank=True, null=True)
    doll_name = models.CharField( max_length=20, blank=True, null=True)
    doll_price = models.IntegerField( null=True, blank=True, default=0)
    doll_description = models.TextField( max_length=30, blank=True, null=True)
    doll_image = models.ImageField(upload_to='doll_images', blank=True, null=True)

    def __str__(self):
        return self.doll_name
    
class DollItem(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    dolls = models.ForeignKey(Doll, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} * {self.dolls}'    

class Procurement(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    dolls = models.ForeignKey(Doll, on_delete=models.CASCADE)  

    def __str__(self):
        return self.baby  

class BabyPayment(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    dolls = models.ForeignKey(Doll, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(null=True, blank=True, default=0)



    def __str__(self):
        return self.baby

class Registered_baby(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    payments = models.ForeignKey(BabyPayment, on_delete=models.CASCADE)    
    
