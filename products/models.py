from django.db import models

# Create your models here.
class product(models.Model):
    
    image = models.ImageField(upload_to = 'pics')
    name =  models.CharField(max_length=100)
    desc = models.TextField()
    sale = models.BooleanField(default=False)
    price1 = models.FloatField()
    price2 = models.FloatField()