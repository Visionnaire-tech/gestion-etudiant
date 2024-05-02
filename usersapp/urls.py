from django.urls import path, include
from django.contrib.auth import views as auth_views
from usersapp import views

urlpatterns =[
	
	path('', views.login , name='login'),
    path('logout/', views.logout_account, name='logout_account'),
	path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name = 'reset_password'),
	path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('register/', views.register_account, name = 'register_account'),
    path('pdf/',views.pdf, name='pdf'),
	path('envoistp/',views.envoistp, name='envoistp'),
	path('info/',views.info, name='info'),
    path('Service/',views.service, name='service'),
    
]