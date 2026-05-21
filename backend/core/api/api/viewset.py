#comment faire les API avec le modele viewsets
from api.models import Product
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from api.api.serializers import ProductSerializer1, ProductSerializer2


class ProductViewSet(ModelViewSet): 
    serializer_class = ProductSerializer1 
    queryset = Product.objects.all() 
