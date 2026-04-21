from api.models import Product
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.api.serializers import ProductSerializer1, ProductSerializer2

#comment developper une api rest avec le decorateur api_view de django rest framework
@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
#GET: pour recuperer les produits
#POST: pour creer un produit
#PUT: pour mettre à jour un produit
#DELETE: pour supprimer un produit
#PATCH: pour mettre à jour partiellement un produit
def product_api_view(request, pk=None, *args, **kwargs):

    if request.method == 'GET':
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)#Si le produit n'existe pas on renvoie une erreur 404
            # data = {'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description}
            #à la place de faire la serialisation manuellement on peut utiliser un serializer pour faire le travail à notre place
            serializer = ProductSerializer1(product) #On peut aussi utiliser ProductSerializer2(product) mais dans ce cas ci on doit definir les champs que l'on veut serialiser et deserialiser dans le serializer, alors que dans ProductSerializer1 on utilise un model serializer qui va automatiquement definir les champs à partir du model, et on peut aussi ajouter des champs qui ne sont pas dans le model, ou faire des calculs à partir des champs du model pour definir des champs qui ne sont pas dans le model, et ces champs seront pris en compte lors de la serialisation et de la deserialisation
            return Response(serializer.data, status=status.HTTP_200_OK) #On peut aussi utiliser return Response(serializer.data) mais c'est mieux de préciser le status de la réponse pour que le client puisse savoir si la requete a réussi ou pas, et quel type de reponse il doit attendre serialiser.data est une representation en format json de l'instance du model, et c'est ce que le client va recevoir dans la reponse de la requete GET
        products = Product.objects.all()
        context = {'request': request} #On peut aussi passer le contexte de la requete au serializer pour que le serializer puisse construire les liens vers les detail view de l'instance du model, on fait cela en passant le contexte de la requete au serializer, et en utilisant HyperlinkedIdentityField dans le serializer pour construire les liens vers les detail view de l'instance du model

        # data = [{'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description} for product in products]
        #à la place de faire la serialisation manuellement on peut utiliser un serializer pour faire le travail à notre place
        serializer = ProductSerializer1(products, many=True, context=context)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #On cree un produit
    if request.method == 'POST':
        # data = request.data #On recupere les données pour la validation
        # name = data.get('name') #On recupere precisement le nom pour la validation
        # price = data.get('price')
        # description = data.get('description')
        # product = Product.objects.create(name=name, price=price, description=description)
        # return Response({'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description}, status=status.HTTP_201_CREATED)
        
        #à la place de faire la deserialisation manuellement on peut utiliser un serializer pour faire le travail à notre place
        # if name in ['Mangue', 'Ananas', 'Citron', 'Orange']:#On verifie si le nom est compris entre cette liste de noms
        #     return Response({'message':'Only electronic categorical'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProductSerializer1(data=request.data) #request.data est un dictionnaire qui contient les données envoyées par le client dans la requete POST, et on passe ce dictionnaire au serializer pour qu'il puisse faire la deserialisation et la validation des données, si les données sont valides le serializer va creer une instance du model à partir des données validées, sinon il va renvoyer les erreurs de validation
        if serializer.is_valid(raise_exception=True): #is_valid() pour valider les données envoyées par le client, si les données sont valides la méthode is_valid() va retourner True, sinon elle va retourner False, et si on passe raise_exception=True la méthode is_valid() va lever une exception ValidationError si les données ne sont pas valides, et cette exception va être gérée par le framework pour renvoyer une réponse avec les erreurs de validation et un status code 400 Bad Request
            serializer.save() #save() pour creer une instance du model à partir des données validées, et pour enregistrer cette instance dans la base de données, si on utilise un model serializer le serializer va automatiquement creer une instance du model à partir des données validées, sinon on doit definir la méthode create() dans le serializer pour faire le travail à notre place
            return Response(serializer.data, status=status.HTTP_201_CREATED) #serializer.data est une representation en format json de l'instance du model qui vient d'être créée, et c'est ce que le client va recevoir dans la reponse de la requete POST
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Si les données ne sont pas valides on renvoie les erreurs de validation et un status code 400 Bad Request
    
    if request.method == 'PUT':
        if pk is None:
            return Response({'message': 'You must provide a pk'}, status=status.HTTP_400_BAD_REQUEST)    
        product = get_object_or_404(Product, pk=pk) #On recupere le produit à mettre à jour, si le produit n'existe pas on renvoie une erreur 404
        serializer = ProductSerializer1(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        if pk is None:
            return Response({'message': 'You must provide a pk'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        if pk is None:
            return Response({'message': 'You must provide a pk'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product ,pk=pk)
        serializer = ProductSerializer1(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)