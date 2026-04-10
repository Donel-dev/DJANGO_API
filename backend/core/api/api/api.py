from matplotlib.pylab import product

from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.api.serializers import ProductSerializer1, ProductSerializer2

#comment developper une api rest avec le decorateur api_view de django rest framework
@api_view(['GET', 'POST'])
def product_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        # data = [{'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description} for product in products]
        #à la place de faire la serialisation manuellement on peut utiliser un serializer pour faire le travail à notre place
        serializer = ProductSerializer2(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        # data = request.data
        # name = data.get('name')
        # price = data.get('price')
        # description = data.get('description')
        # product = Product.objects.create(name=name, price=price, description=description)
        # return Response({'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description}, status=status.HTTP_201_CREATED)
        
        #à la place de faire la deserialisation manuellement on peut utiliser un serializer pour faire le travail à notre place
        serializer = ProductSerializer1(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)