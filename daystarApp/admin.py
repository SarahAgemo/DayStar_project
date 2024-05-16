from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Sign_in)
admin.site.register(Doll)



admin.site.register(BabyDeparture)
admin.site.register(BabyPayment)
admin.site.register(Sitterform)
admin.site.register(Sitter_arrival)
admin.site.register(Sitter_departure)
admin.site.register(Sitter_payment)
admin.site.register(Doll_payment)