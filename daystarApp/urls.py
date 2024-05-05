from django.urls import path
from . import views


urlpatterns = [
    #index
    path('', views.index, name='index'),

    #about 
    path('about_us/', views.about_us, name='about_us'),


    #babies

    #baby registration
    path('beb_reg_form/', views.beb_reg_form, name='beb_reg_form'),
    path('baby_add/', views.baby_add, name='baby_add'),
    path('baby_view/<int:id>/', views.baby_view, name='baby_view'),
    path('baby_edit/<int:id>/', views.baby_edit, name='baby_edit'),
    

    #baby arrival
    path('baby_arrival/', views.baby_arrival, name='baby_arrival'),
    path('baby_adds/', views.baby_adds, name='baby_adds'),
    path('baby_views/<int:id>/', views.baby_views, name='baby_views'),
    path('baby_edits/<int:id>/', views.baby_edits, name='baby_edits'),

    #baby departure
    path('baby_depart/', views.baby_depart, name='baby_depart'),
    path('depart_views/<int:id>/', views.depart_views, name='depart_views'),
    path('depart_edits/<int:id>/', views.depart_edits, name='depart_edits'),
    path('depart_adds/', views.depart_adds, name='depart_adds'),

    #baby payment
    path('baby_pay/', views.baby_pay, name='baby_pay'),
   
    
    
    

    #dolls/stock
   
    path('dolls/', views.dolls, name='dolls'),
    path('stock/', views.stock, name='stock'),


    

    #sitters

    #sitter registration 
    path('sit_reg_form/', views.sit_reg_form, name='sit_reg_form'),
    path('sit_add/', views.sit_add, name='sit_add'),
    path('sit_view/<int:id>/', views.sit_view, name='sit_view'),
    path('sit_edit/<int:id>/', views.sit_edit, name='sit_edit'),
    


    #Arrivals urls
    path('sit_arrival/', views.sit_arrival, name='sit_arrival'),
    path('sit_adds/', views.sit_adds, name='sit_adds'),
    path('sit_views/<int:id>/', views.sit_views, name='sit_views'),
    path('sit_edits/<int:id>/', views.sit_edits, name='sit_edits'),

    #departure urls
    path('sit_depart/', views.sit_depart, name='sit_depart'),
    path('depart_view/<int:id>/', views.depart_view, name='depart_view'),
    path('depart_edit/<int:id>/', views.depart_edit, name='depart_edit'),
    path('depart_add/', views.depart_add, name='depart_add'),
  
    #sitter payments
    path('sit_payments/', views.sit_payments, name='sit_payments'),


  
    
    #authentication
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('forgot_pass/', views.forgot_pass, name='forgot_pass'),
    path('reset_pass/', views.reset_pass, name='reset_pass'),
    path('new_pass/', views.new_pass, name='new_pass'),
    
        
]