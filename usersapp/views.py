from django.shortcuts import render, redirect , HttpResponse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from usersapp.forms import UserRegistrationForm , TPS , Forml1lmdjour
from django.contrib.auth import login, authenticate ,logout
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import TP , Etudiant ,L1lmdjour
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import password_validation


def login(request):
    # test so connecter
    if request.user.is_authenticated:
        return redirect('home')

    else:

        if request.method == "POST":

            # get data in form input
            username = request.POST["nomUtilisateur"]
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

def pdf(request):
    return render(request, 'pdf.html')

#
def logout_user(request):			
    logout(request)
    return redirect('login')

def conf(request):
	return render(request,'conf.html')


def info(request):
	return render(request,'about.html')

def service(request):
	return render(request,'service.html')   

@permission_required('usersapp.view_tp')
def envoistp(request):
    if request.user.groups.filter(name='Paiement').exists():
        if request.method == "POST":

            nom = request.POST.get("nom")

            postnoms = request.POST.get("postnom")

            prenoms = request.POST.get("prenom")

            promotion = request.POST.get("promotion")

            travail = request.POST.get("travail")

            if L1lmdjour.objects.filter(Nom=nom).exists():
                messages.error(request, "Désolé votre Travail été déjà envoyé")
                return redirect('envoistp')

            Forml1lmdjour = L1lmdjour.objects.create(Nom=nom, Postnom=postnoms, Prenom=prenoms, Promotion=promotion,  Séléctionner_Votre_travail=travail)
            Forml1lmdjour.save()
            return redirect('home')

        else:
            return render(request, "envoistp.html")
    else:
         return render(request,'conf.html')