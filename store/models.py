from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.CharField(max_length=200, default="")  # URL or local path

    def _str_(self):
        return self.namefrom django.db import models

# Create your models here.
