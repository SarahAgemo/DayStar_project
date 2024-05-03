from django.urls import path
from . import views


urlpatterns = [
    #index
    path('', views.index, name='index'),

    #about 
    path('about_us/', views.about_us, name='about_us'),

    #babies
    path('baby_arrival/', views.baby_arrival, name='baby_arrival'),
    path('baby_depart/', views.baby_depart, name='baby_depart'),
    path('baby_pay/', views.baby_pay, name='baby_pay'),
    path('beb_reg_form/', views.beb_reg_form, name='beb_reg_form'),
    
    
    

    #dolls
   
    path('dolls/', views.dolls, name='dolls'),
    path('stock/', views.stock, name='stock'),
    

    #sitters
    
    path('sit_arrival/', views.sit_arrival, name='sit_arrival'),
    path('sit_depart/', views.sit_depart, name='sit_depart'),
    path('sit_payments/', views.sit_payments, name='sit_payments'),
   #sitter registration 
    path('sit_reg_form/', views.sit_reg_form, name='sit_reg_form'),
    path('sit_add/', views.sit_add, name='sit_add'),
    path('sit_view/<int:id>/', views.sit_view, name='sit_view'),
    path('sit_edit/<int:id>/', views.sit_edit, name='sit_edit'),
    
    
    #authentication
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('forgot_pass/', views.forgot_pass, name='forgot_pass'),
    path('reset_pass/', views.reset_pass, name='reset_pass'),
    path('new_pass/', views.new_pass, name='new_pass'),
    
        
]