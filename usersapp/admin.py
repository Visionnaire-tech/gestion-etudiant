from django.contrib import admin
from .models import *
# Register your models here.
class EtudiantModelAdmin(admin.ModelAdmin):
    list_display = ('postnom', 'prenom','promotions','vacations')


class L1lmdjourModelAdmin(admin.ModelAdmin):
    list_display = ('Nom', 'Postnom','Prenom','Promotion')

admin.site.register(Etudiant,EtudiantModelAdmin)
admin.site.register(L1lmdjour,L1lmdjourModelAdmin)
admin.site.register(TP)

admin.site.register(Note)
admin.site.register(Note1)
admin.site.register(Note2)
