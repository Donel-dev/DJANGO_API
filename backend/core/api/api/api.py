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
            serializer = ProductSerializer1(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        products = Product.objects.all()
        # data = [{'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description} for product in products]
        #à la place de faire la serialisation manuellement on peut utiliser un serializer pour faire le travail à notre place
        serializer = ProductSerializer2(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #On cree un produit
    if request.method == 'POST':
        data = request.data #On recupere les données pour la validation
        name = data.get('name') #On recupere precisement le nom pour la validation
        # price = data.get('price')
        # description = data.get('description')
        # product = Product.objects.create(name=name, price=price, description=description)
        # return Response({'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description}, status=status.HTTP_201_CREATED)
        
        #à la place de faire la deserialisation manuellement on peut utiliser un serializer pour faire le travail à notre place
        if name in ['Mangue', 'Ananas', 'Citron', 'Orange']:#On verifie si le nom est compris entre cette liste de noms
            return Response({'message':'Only electronic categorical'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProductSerializer1(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        if pk is None:
            return Response({'message': 'You must provide a pk'}, status=status.HTTP_400_BAD_REQUEST)    
        product = get_object_or_404(Product, pk=pk)
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