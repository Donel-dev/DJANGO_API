from django.urls import path

from api.api.api import product_api_view

from .views import home

app_name = 'api'

urlpatterns = [
    path('', home, name='home'),
    path('product/', product_api_view, name='product_api_view'),
    path('product/<int:pk>/', product_api_view, name='product_api_view'),
]
