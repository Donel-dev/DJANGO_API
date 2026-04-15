from api.models import Product
from rest_framework import serializers


class ProductSerializer1(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)#On peut ajouter des champs qui ne sont pas dans le model, mais qui seront pris en compte lors de la serialisation et de la deserialisation
    #Le champ email ne sera pas pris en compte lors de la serialisation (lorsqu'on va convertir l'instance du model en json), mais il sera pris en compte lors de la deserialisation (lorsqu'on va convertir le json en instance du model)c'est pour cela qu'on utilise write_only=True
    class Meta:
        model = Product
        #La serialisation et la deserialisation vont se faire sur tout les champs du model
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']#Ces champs ne seront pas pris en compte lors de la deserialisation; ils seront juste utilser pour la serialisation 

    def create(self, validated_data):
        email = validated_data.pop('email')#On peut recuperer les champs qui ne sont pas dans le model et les utiliser pour faire des operations avant de creer l'instance du model
        print(f"Email: {email}")
        return super().create(validated_data)
        

#Dans ce cas ci on ne tient pas compte du model et on va juste definir les champs que l'on veut serialiser et deserialiser
#Avec ce serialiser on ne peut cree un champ automatiquement dans la base de données, on doit le faire manuellement dans la vue, ou en faisant une surcharge de la méthode create du serializer pour faire le travail à notre place
#
class ProductSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(max_length=500)

#Comme on n'utilise pas un model serializer, on doit definir la méthode create pour pouvoir creer une instance du model à partir des données validées
    def create(self, validated_data):
        return Product.objects.create(**validated_data)