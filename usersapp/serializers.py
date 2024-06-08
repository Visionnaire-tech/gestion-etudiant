from rest_framework.serializers import ModelSerializer
 
from .models import Etudiant
 
class CategorySerializer(ModelSerializer):
 
    class Meta:
        model = Etudiant
        fields = ['id', 'postnom','prenom','cursus']
