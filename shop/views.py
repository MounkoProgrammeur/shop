from django.shortcuts import render, redirect
from .models import Produit, Categorie



def home(request):
    return render(request, "home.html")


def ajouter_produit(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        categorie_id = request.POST['categorie']
        description = request.POST.get('description', '')
        image_file = request.FILES.get('image')  # Fichier uploadé depuis le formulaire

        produit = Produit(
            title=title,
            price=price,
            description=description,
            categorie_id=categorie_id
        )

       
        produit.image_file = image_file

        produit.save()
        return redirect('liste_produits')

    categories = Categorie.objects.all()
    return render(request, 'ajouter_produit.html', {'categories': categories})



def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'liste_produits.html', {'produits':produits})
