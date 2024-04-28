from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from usersapp.models import TP , L1lmdjour


class UserRegistrationForm(UserCreationForm):
	last_name= forms.CharField(label='Nom')
	first_name= forms.CharField(label='Post_Nom')
	first= forms.CharField(label='Prénom')
	email = forms.EmailField(label='Adresse e-mail')
	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields + ( 'last_name','first_name','first' , 'email')

class TPS(forms.ModelForm):
    class Meta:
        model = TP 
        exclude = ('fiends',)

class Forml1lmdjour(forms.ModelForm):
    class Meta:
        model = L1lmdjour 
        exclude = ('fiends',)