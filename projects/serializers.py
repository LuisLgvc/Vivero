from rest_framework import serializers
from .models import Riego, Ambientes, Macetas, Plantas

class RiegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riego
        fields = '__all__'
        
class AmbientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambientes
        fields = '__all__'

class MacetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macetas
        fields = '__all__'
        
class PlantasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantas
        fields = '__all__'
        read_only_fields = ['actualizado']