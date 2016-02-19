from rest_framework import serializers
from detransapp.models import Bloco



class BlocoSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = Bloco
        fields = ('inicio_intervalo', 'fim_intervalo', 'data', 'data_alterado', 'ativo', 'contador', 'usuario',)
