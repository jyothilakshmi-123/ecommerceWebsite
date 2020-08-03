from django.shortcuts import render
from .models import product

# Create your views here.
def shop(request):
    prods = product.objects.all()

    return render(request,'shop.html',{'prods':prods})