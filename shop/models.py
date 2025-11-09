from django.db import models
from django.conf import settings
from supabase import create_client
import uuid


supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

class Categorie(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

class Produit(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categorie')
    image_url = models.URLField(blank=True, null=True)  
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):
        
        image_file = getattr(self, "image_file", None)
        if image_file:
            filename = f"{uuid.uuid4()}_{image_file.name}"
            supabase.storage.from_(settings.SUPABASE_BUCKET).upload(filename, image_file.read())
            self.image_url = f"{settings.SUPABASE_PUBLIC_URL}/{filename}"
            delattr(self, "image_file")  
        super().save(*args, **kwargs)
