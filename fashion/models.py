from django.db import models

# Create your models here.
class Specialday(models.Model):
   
    catagory = models.CharField(max_length=100)
    day_name = models.CharField(max_length=100)
    desc = models.TextField()
    img  = models.ImageField(upload_to='pics')
    sale = models.BooleanField(default = False)