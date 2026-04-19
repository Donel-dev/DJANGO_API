from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("api:product_api_view_detail", kwargs={"pk": self.pk}) #On peut definir une methode get_absolute_url dans le model pour retourner l'url de la detail view de l'instance du model, et cette methode sera disponible lors de la serialisation et de la deserialisation, on peut utiliser cette methode pour construire le lien vers la detail view de l'instance du model dans le serializer
    
    def get_price_in_euros(self): #On peut definir des methodes dans le model pour faire des operations sur les champs du model, et ces methodes seront disponibles lors de la serialisation et de la deserialisation   
        return f"{self.price}"
    
    def get_description(self): 
        return f"{self.name} - {self.price}"
    
    def __str__(self):
        return self.name
