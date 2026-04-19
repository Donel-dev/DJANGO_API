from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import Product

@csrf_exempt #On utilise ce decorateur pour desactiver la protection contre les attaques CSRF pour cette vue, car on va faire des requetes POST depuis un client qui n'est pas le navigateur, et le navigateur n'enverra pas le token CSRF dans les requetes POST, donc on doit desactiver la protection contre les attaques CSRF pour cette vue
def home(request):
    headers = request.headers #On peut aussi acceder aux headers de la requete pour faire des operations en fonction des headers, par exemple pour faire du versioning de l'API en utilisant un header custom pour indiquer la version de l'API que le client utilise
    params = request.GET.get('q') #On peut aussi acceder aux parametres de la requete pour faire des operations en fonction des parametres, par exemple pour faire du filtering de l'API en utilisant un parametre pour indiquer les criteres de filtrage
    
    if request.method == 'POST':

        post_data = request.body #On peut acceder au corps de la requete pour recuperer les données envoyées par le client dans une requete POST, le corps de la requete est une chaine de caracteres en format json, donc on doit la convertir en dictionnaire python en utilisant la fonction json.loads() pour pouvoir acceder aux données envoyées par le client
    
        data = json.loads(post_data)
        name = data.get('name') #On peut acceder aux données envoyées par le client en utilisant la méthode get() du dictionnaire, pour eviter les erreurs si la clé n'existe pas dans le dictionnaire, on peut aussi utiliser data['name'] mais cela va generer une erreur si la clé 'name' n'existe pas dans le dictionnaire
        price = data.get('price')
        description = data.get('description')

        product = Product.objects.create(
            name=name,
            price=price,
            description=description,
        )
        
        return JsonResponse({
            'id':product.id,
            'name':product.name,
            'price':product.price,
            'description':product.description
        })
    products = Product.objects.all()
    data = [{'id':product.id, 'name':product.name} for product in products]

    return JsonResponse(data, safe=False)










