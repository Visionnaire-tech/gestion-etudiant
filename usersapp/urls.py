from django.urls import path, include
from django.contrib.auth import views as auth_views
from usersapp.views import *

urlpatterns =[
	
	path('', login , name='login'),
    path('logout/', logout_account, name='logout_account'),
	path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name = 'reset_password'),
	path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('register_account/', register_account, name = 'register_account'),
    path('pdf/',pdf, name='pdf'),
	path('envoistp/',envoistp, name='envoistp'),
	path('info/',info, name='info'),
    path('Service/',service, name='service'),
    path('produit/',produit_list),
    path('produit/<int:id>/',produit_detail),
    path('accueil',home, name='home'),
	path('Resolution',exer, name='exer'),
    
]