from django.db import models

class  product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        self.name



# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True)
    description = models.TextField()

    def __str__(self):
      return  self.title



