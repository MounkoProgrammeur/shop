from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    
    image_file = forms.ImageField(required=True)

    class Meta:
        model = Produit
        fields = ['title', 'price', 'description', 'categorie', 'image_file']
