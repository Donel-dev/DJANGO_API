from api.models import Product
from rest_framework import serializers


class ProductSerializer1(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)#On peut ajouter des champs qui ne sont pas dans le model, mais qui seront pris en compte lors de la serialisation et de la deserialisation
    #Le champ email ne sera pas pris en compte lors de la serialisation (lorsqu'on va convertir l'instance du model en json), mais il sera pris en compte lors de la deserialisation (lorsqu'on va convertir le json en instance du model)c'est pour cela qu'on utilise write_only=True
    name = serializers.CharField(max_length=255)
    price_in_euros = serializers.SerializerMethodField()#On peut aussi definir des champs qui ne sont pas dans le model, mais qui seront calculés à partir des champs du model, et ces champs seront pris en compte lors de la serialisation et de la deserialisation
    #description = serializers.CharField(max_length=500, source='get_description')#On peut aussi definir des champs qui ne sont pas dans le model, mais qui seront calculés à partir des champs du model, et ces champs seront pris en compte lors de la serialisation et de la deserialisation; on utilise source pour indiquer la méthode du model qui va calculer la valeur de ce champ
    description_in_euros = serializers.SerializerMethodField()
    #detail_link = serializers.HyperlinkedIdentityField(view_name='product-detail')#On peut aussi definir des champs qui ne sont pas dans le model, mais qui seront calculés à partir des champs du model, et ces champs seront pris en compte lors de la serialisation et de la deserialisation; on utilise HyperlinkedIdentityField pour creer un lien vers la detail view de l'instance du model
    #detail_link = serializers.SerializerMethodField() #MethodField pour creer un champ qui va calculer sa valeur à partir d'une méthode du serializer, on doit definir une methode get_<field_name> pour calculer la valeur de ce champ
    #detail_link = serializers.CharField(source='get_absolute_url')#On peut aussi definir des champs qui ne sont pas dans le model, mais qui seront calculés à partir des champs du model, et ces champs seront pris en compte lors de la serialisation et de la deserialisation; on utilise source pour indiquer la méthode du model qui va calculer la valeur de ce champ
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_view_detail', lookup_field='pk')#On peut aussi definir des champs qui ne sont pas dans le model, mais qui seront calculés à partir des champs du model, et ces champs seront pris en compte lors de la serialisation et de la deserialisation; on utilise HyperlinkedIdentityField pour creer un lien vers la detail view de l'instance du model, on doit indiquer le nom de la view et le champ qui va servir de lookup pour construire l'url, lookup_field='pk' pour utiliser le champ pk de l'instance du model pour construire l'url
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'email', 'price_in_euros', 'description_in_euros', 'link']#On peut aussi definir les champs que l'on veut serialiser et deserialiser
        #excludes = ['created_at', 'updated_ at']#On peut aussi definir les champs que l'on ne veut pas serialiser et deserialiser

    def get_price_in_euros(self, obj):#On doit definir une methode pour calculer la valeur du champ price_in_euros; le nom de la methode doit etre get_<field_name>
        return obj.get_price_in_euros() #On peut aussi faire le calcul directement dans la methode get_price_in_euros, mais c'est mieux de deleguer le travail au model pour respecter le principe de separation des responsabilites
    
    def get_description_in_euros(self, obj):
        return obj.get_description() #On peut aussi faire le calcul directement dans la methode get_description_in_euros, mais c'est mieux de deleguer le travail au model pour respecter le principe de separation des responsabilites
    
    def get_detail_link(self, obj):
        return obj.get_absolute_url() #On peut aussi faire le calcul directement dans la methode get_detail_link, mais c'est mieux de deleguer le travail au model pour respecter le principe de separation des responsabilites

    def validate_name(self, value): #validate_<field_name> pour valider un champ en particulier or dans django forms c'etait clean_<field_name>
        if value in ['Mangue', 'Ananas', 'Citron', 'Orange']:#On verifie si le nom est compris entre cette liste de noms
            raise serializers.ValidationError('Only electronic categorical')
        return value #Si le nom est valide, on le retourne pour qu'il soit pris en compte dans la deserialisation
    
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