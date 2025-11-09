from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('produits/', views.liste_produits, name="liste_produits"),
    path('ajouter/', views.ajouter_produit, name="ajouter_produit")
]
