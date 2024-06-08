from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
	
    def __str__(self):
        return self.title
    
class Note1(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
	
    def __str__(self):
        return self.title
    
class Note2(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
	
    def __str__(self):
        return self.title


class Etudiant(models.Model):
    user = models.OneToOneField('auth.User', related_name='etudiant',on_delete= models.CASCADE)

    postnom = models.CharField(max_length=256)
    prenom = models.CharField(max_length=256)

    sexe = models.CharField(blank=True, null=True,
                            choices=(('Homme', 'Homme'), ('Femme', 'Femme')), max_length=256)
    cursus = models.CharField(blank=True, null=True,
                            choices=(('Gestion Informatique', 'Gestion Informatique'), ('Réseau', 'Réseau')), max_length=256)
    promotions = models.CharField(blank=True, null=True,
                            choices=(('L1 LMD', 'L1 LMD'), ('L2 LMD', 'L2 LMD'), ('L3 LMD', 'L3 LMD')), max_length=256)

    vacations = models.CharField(blank=True, null=True,
                            choices=(('Jour', 'Jour'), ('Soir', 'Soir')), max_length=256)

    adresse = models.CharField(max_length=256, blank=True, null=True)

    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=256, blank=True, null=True)

    telephone = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self) -> str:
        return self.postnom +" "+  self.prenom

class TP(models.Model):
    Séléctionner_Votre_travail = models.FileField(upload_to='PDF')

class L1lmdjour(models.Model):
    Nom = models.CharField(max_length=60)
    Postnom = models.CharField(max_length=60)
    Prenom = models.CharField(max_length=60)
    Promotion = models.CharField(max_length=60)
    Séléctionner_Votre_travail = models.FileField(upload_to='PDF')
    def __str__(self) -> str:
        return self.Nom +" "+  self.Postnom +" "+  self.Prenom +" "+  self.Promotion

class L1lmdsoir(models.Model):
    Nom = models.CharField(max_length=60)
    Postnom = models.CharField(max_length=60)
    Prenom = models.CharField(max_length=60)
    Promotion = models.CharField(max_length=60)
    Séléctionner_Votre_travail = models.FileField(upload_to='PDF')

class L3lmdjour(models.Model):
    Nom = models.CharField(max_length=60)
    Postnom = models.CharField(max_length=60)
    Prenom = models.CharField(max_length=60)
    Promotion = models.CharField(max_length=60)
    Séléctionner_Votre_travail = models.FileField(upload_to='PDF')

class L3lmdsoir(models.Model):
    Nom = models.CharField(max_length=60)
    Postnom = models.CharField(max_length=60)
    Prenom = models.CharField(max_length=60)
    Promotion = models.CharField(max_length=60)
    Séléctionner_Votre_travail = models.FileField(upload_to='PDF')

class L1(models.Model):
    Nom = models.CharField(max_length=60)
    Postnom = models.CharField(max_length=60)
    Prenom = models.CharField(max_length=60)
    Promotion = models.CharField(max_length=60)
    Séléctionner_Votre_travail = models.FileField(upload_to='PDF')
    