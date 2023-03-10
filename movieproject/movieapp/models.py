from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=254)
    description=models.TextField()
    year=models.IntegerField()
    Stars=models.CharField(max_length=241)
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name