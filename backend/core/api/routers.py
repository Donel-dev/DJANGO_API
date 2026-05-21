from django.urls import path
from api.api.viewset import ProductViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

"""
default router est utilisé pour les operations CRUD
par contre le simple router est utiliser pour les operations de lecture
"""

router = DefaultRouter() #cette ligne de code est utilisée pour les opérations CRUD, elle sert à créer automatiquement les routes pour les opérations de création, lecture, mise à jour et suppression (CRUD) pour les vues basées sur des ensembles de vues (viewsets).
router.register('v1/product', ProductViewSet, basename='product') #cette ligne de code enregistre une vue basée sur un ensemble de vues (viewset) appelée ProductViewSet auprès du routeur. Le premier argument 'v1/product' spécifie le préfixe de l'URL pour les routes générées, tandis que le troisième argument basename='product' est utilisé pour nommer les routes générées, ce qui facilite leur utilisation dans d'autres parties de l'application.
urlpatterns = router.urls # cette ligne de code assigne les URL générées par le routeur à la variable urlpatterns, qui est utilisée par Django pour déterminer quelles vues doivent être appelées en fonction des URL demandées. En résumé, ce code configure les routes pour les opérations CRUD sur les produits en utilisant un routeur de Django REST Framework.

#le lien de ca avec le fichiers urls.py est que dans le fichier urls.py, on importe les urlpatterns de ce fichier routers.py pour les inclure dans les routes globales de l'application Django. Cela permet de centraliser la gestion des routes liées aux produits dans ce fichier routers.py, tout en les rendant accessibles à l'ensemble de l'application via le fichier urls.py.
#exemple d'endpoint : http://localhost:8000/api/v1/product/ pour accéder à la liste des produits ou pour créer un nouveau produit, et http://localhost:8000/api/v1/product/<id>/ pour accéder, mettre à jour ou supprimer un produit spécifique en fonction de son ID.
#DefaultRouter est utilisé pour les opérations CRUD, tandis que SimpleRouter est utilisé pour les opérations de lecture.