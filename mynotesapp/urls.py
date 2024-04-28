from django.urls import path
from mynotesapp import views

urlpatterns =[
	path('accueil',views.home, name='home'),
	path('Resolution',views.exer, name='exer'),
]
