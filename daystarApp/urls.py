from django.urls import path
from . import views


urlpatterns = [
    #index
    path('', views.index, name='index'),


    #homepage
    path('home/', views.home, name='home'),

    #about 
    path('about_us/', views.about_us, name='about_us'),


    #babies

    #baby registration
    path('beb_reg_form/', views.beb_reg_form, name='beb_reg_form'),
    path('baby_add/', views.baby_add, name='baby_add'),
    path('baby_view/<int:id>/', views.baby_view, name='baby_view'),
    path('baby_edit/<int:id>/', views.baby_edit, name='baby_edit'),
    

    #baby arrival
   
    #baby departure
    path('baby_depart/', views.baby_depart, name='baby_depart'),
    path('depart_baby_view/<int:baby_id>/', views.depart_baby_view, name='depart_baby_view'),
    path('depart_baby_edit/<int:baby_id>/', views.depart_baby_edit, name='depart_baby_edit'),
    path('depart_baby_add/', views.depart_baby_add, name='depart_baby_add'),

    #baby payment
    path('baby_pay/', views.baby_pay, name='baby_pay'),
    path('add_baby_payment/', views.add_baby_payment, name='add_baby_payment'),
    path('edit_baby_payment/<int:id>/', views.edit_baby_payment, name='edit_baby_payment'),
    
    #baby_receipt
    path('baby_receipt/', views.baby_receipt, name='baby_receipt'),

    #baby_receipt detail
   path('baby_receipt_detail/<int:id>/', views.baby_receipt_detail, name='baby_receipt_detail'),
   
    

    #dolls
    #doll list
    path('doll_list/', views.doll_list, name='doll_list'),

    #doll add
    path('add_doll', views.add_doll, name='add_doll'),

    #doll view
    path('doll_view/<int:id>/', views.doll_view, name='doll_view'),

    #add one doll
    path('add_one_doll/<int:id>/', views.add_one_doll, name='add_one_doll'),

    #doll edit
    path('doll_edit/<int:id>/', views.doll_edit, name='doll_edit'),
    
    #doll pay
    path('doll_pay/<int:id>/', views.doll_pay, name='doll_pay'),

    path('doll_pay_list', views.doll_pay_list, name='doll_pay_list'),

    #doll receipt
    path('doll_receipt', views.doll_receipt, name='doll_receipt'),

    #receipt detail
    path('receipt_detail/<int:id>/', views.receipt_detail, name='receipt_detail'),



    #stock
    path('stock_list/', views.stock_list, name='stock_list'),

    #stock add all
    path('add_stock', views.add_stock, name='add_stock'),

    #view one stock 
    path('stock_view/<int:id>/', views.stock_view, name='stock_view'),

    #stock add one
    path('add_one_stock/<int:id>/', views.add_one_stock, name='add_one_stock'),

    #stock issue
    path('stock_issue/<int:id>/', views.stock_issue, name='stock_issue'),

    #stock edit
    path('stock_edit/<int:id>/', views.stock_edit, name='stock_edit'),




    

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
    path('add_sit_payment/', views.add_sit_payment, name='add_sit_payment'),


  
    
    #authentication
    path('sign_in/', views.sign_in, name='sign_in'),
    
    # path('forgot_pass/', views.forgot_pass, name='forgot_pass'),
    # path('reset_pass/', views.reset_pass, name='reset_pass'),
    # path('new_pass/', views.new_pass, name='new_pass'),
    
        
]