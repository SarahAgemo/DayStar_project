from django.urls import path
from . import views


urlpatterns = [
    #index
    path('', views.index, name='index'),

    #about 
    path('about_us/', views.about_us, name='about_us'),

    #babies
    path('baby_attend/', views.baby_attend, name='baby_attend'),
    path('baby_comments/', views.baby_comments, name='baby_comments'),
    path('baby_pay/', views.baby_pay, name='baby_pay'),
    path('beb_reg_form/', views.beb_reg_form, name='beb_reg_form'),
    path('baby_list/', views.baby_list, name='baby_list'),
    path('add_baby/', views.add_baby, name='add_baby'),
    path('view_bebs/<int:baby_id>', views.view_bebs, name='view_bebs'),

    #dolls
    # path('add_to_dolls/', views.add_to_dolls, name='add_to_dolls'),
    # path('remove_from_dolls/', views.remove_from_dolls, name='remove_from_dolls'),
    # path('view_dolls/', views.view_dolls, name='view_dolls'),
    path('pro_dolls/', views.pro_dolls, name='pro_dolls'),
    # path('doll_list/', views.doll_list, name='doll_list'),
    

    #sitters
    path('sit_comments/', views.sit_comments, name='sit_comments'),
    path('sit_attend/', views.sit_attend, name='sit_attend'),
    path('sit_ass_babes/', views.sit_ass_babes, name='sit_ass_babes'),
    path('sit_payments/', views.sit_payments, name='sit_payments'),
    path('sit_reg_form/', views.sit_reg_form, name='sit_reg_form'),
    path('view_sit/', views.view_sit, name='view_sit'),
    
    #authentication
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('forgot_pass/', views.forgot_pass, name='forgot_pass'),
    path('reset_pass/', views.reset_pass, name='reset_pass'),
    path('new_pass/', views.new_pass, name='new_pass'),
    
        
]