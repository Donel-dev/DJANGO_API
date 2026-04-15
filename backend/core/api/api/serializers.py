from api.models import Product
from rest_framework import serializers


class ProductSerializer1(serializers.ModelSerializer):
    email = serializers.EmailField()#On peut ajouter des champs qui ne sont pas dans le model, mais qui seront pris en compte lors de la serialisation et de la deserialisation
    class Meta:
        model = Product
        #La serialisation et la deserialisation vont se faire sur tout les champs du model
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']#Ces champs ne seront pas pris en compte lors de la deserialisation; ils seront juste utilser pour la serialisation 


#Dans ce cas ci on ne tient pas compte du model et on va juste definir les champs que l'on veut serialiser et deserialiser
class ProductSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(max_length=500)
