from django.shortcuts import render, redirect , HttpResponse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from usersapp.forms import *
from django.contrib.auth import login, authenticate ,logout
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import password_validation
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer



@login_required
def home(request):
    context ={
	'voir': Etudiant.objects.filter(),
    }
    return render(request, 'home.html',context)
             
@login_required	
def exer(request):
    context ={
	'notes': Note.objects.filter(),
    'note1': Note1.objects.filter(),
    'note2': Note2.objects.filter()
	}
    return render(request, 'service.html',context)
# Create your views here.
@api_view()
def produit_list(request):
    queryset = Etudiant.objects.all()
    serializer = CategorySerializer(queryset,many=True)
    return Response(serializer.data)

@api_view()
def produit_detail(request,id):
    produit = get_object_or_404(Etudiant,pk=id)
    serializer = CategorySerializer(produit)
    return Response(serializer.data)


def login(request):
    # test so connecter
    if request.user.is_authenticated:
        return redirect('home')

    else:

        if request.method == "POST":

            # get data in form input
            username = request.POST["nomUtilisateur1"]
            password = request.POST["password"]

            # get user
            user = auth.authenticate(request, username=username, password=password)

            # test si utilisateur exist
            if user is not None:
                auth.login(request, user)
                return redirect('home')

            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrecte !")

                return redirect('login')

        else:
            return render(request, "registration/login.html", {})

def logout_account(request):
    auth.logout(request)
    return redirect('login')

def register_account(request):
    if request.method == "POST":

        username = request.POST.get("nomUtilisateur")

        postnom = request.POST.get("postnom")

        prenom = request.POST.get("prenom")

        email = request.POST.get("email")

        password = request.POST.get("motDePasse")

        confirm_password = request.POST.get("confirmeMotDePasse")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe deja")
            return redirect('register_account')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Cette adresse mail existe deja")
            return redirect('register_account')

        if password != confirm_password:
            messages.error(request, "Mot de passe different")
            return redirect('register_account')

        try:
            password_validation.validate_password(password=password)

        except:
            messages.error(request, "Mot de passe non valide")
            return redirect('register_account')

        user = User.objects.create_user(username=username, email=email, password=password)

        user.first_name = postnom

        user.last_name = prenom

        user.save()

        etudiant = Etudiant.objects.create(user=user, postnom=postnom, prenom=prenom)
        etudiant.save()

        messages.success(request, "Merci pour votre enregistrement")

        auth.logout(request)

        return redirect('home')

    else:
        return render(request, "registration/register.html")
@login_required
def pdf(request):
    return render(request, 'pdf.html')

@login_required
def logout_user(request):			
    logout(request)
    return redirect('login')

def conf(request):
	return render(request,'conf.html')


def info(request):
	return render(request,'about.html')

def service(request):
	return render(request,'service.html')   

def envoistp(request):
    if request.user.groups.filter(name='paiement').exists():
        if request.method == 'POST':
            form = Forml1lmdjour(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = Forml1lmdjour()
            # pointer vers le fichier du template index.html
            return render(request, 'envoistp.html' , {'form': form})
    else:
         return render(request,'conf.html')