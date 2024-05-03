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
    baby_name = models.CharField( max_length=20)
    baby_gender = models.CharField( max_length=20 )
    baby_age = models.IntegerField( default=0)
    baby_location = models.CharField( max_length=20)
    # baby_image = models.ImageField(upload_to='baby_images', blank=True, null=True)
    parents_name = models.CharField( max_length=20)
    period_of_stay = models.CharField(choices=[('half-day', 'Half-day'),('full-day', 'Full-day')], max_length=100)
    registration_date = models.DateField(default=timezone.now)
   

    def __str__(self):
        return self.baby_name

    
class Departure(models.Model):
    baby_id = models.AutoField(primary_key=True)
    name_of_baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    baby_picker = models.CharField( max_length=20)
    date_of_departure = models.DateField(default=timezone.now)
    time_out = models.TimeField()
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name_of_baby    

#sitter
class Sitterform(models.Model):  
    name=models.CharField(max_length=200)
    gender=models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=100)
    location=models.CharField(choices=[('kabalagala', 'kabalagala')], max_length=100)
    date_of_birth=models.DateField(default=timezone.now) 
    next_of_kin=models.CharField( max_length=200)
    national_identification_number=models.CharField(max_length=200)
    recommenders_name=models.CharField(max_length=200)
    religon=models.CharField(max_length=200,null=True, blank=True)
    level_of_education=models.CharField( choices=[('degree','Degree'),('diploma','Diploma'),('highschool certificate','Highschool certificate'),('others','Others')],max_length=200)
    sitter_number=models.IntegerField(default=0)
    contacts=models.CharField(max_length=200) 
    date=models.DateField()
    def __str__(self):
        return self.name

class Sitter_arrival(models.Model):
    sitter_name=models.ForeignKey(Sitterform, on_delete=models.CASCADE) 
    sitter_number=models.IntegerField(default=0)
    date_of_arrival=models.DateField(default=timezone.now)   
    timein=models.TimeField ()
    Attendancestatus=models.CharField(choices=[('onduty', 'onduty')], max_length=100)
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

class Arrival(models.Model):
    baby_id = models.AutoField(primary_key=True)
    babys_name = models.ForeignKey(Baby, on_delete=models.CASCADE)
    baby_bringer = models.CharField( max_length=20)
    date_of_arrival = models.DateField(default=timezone.now)
    time_in = models.TimeField()
    Assigned_to=models.ForeignKey(Sitter_arrival,on_delete=models.CASCADE)

    def __str__(self):
       return self.babys_name
    
# class Sitter_payment(models.Model):    


# dolls
class Doll(models.Model):
    doll_type = models.CharField( max_length=20, blank=True, null=True)
    doll_name = models.CharField( max_length=20, blank=True, null=True)
    doll_price = models.IntegerField( null=True, blank=True, default=0)
    doll_description = models.TextField( max_length=30, blank=True, null=True)
    doll_image = models.ImageField(upload_to='doll_images', blank=True, null=True)

    def __str__(self):
        return self.doll_name
    
