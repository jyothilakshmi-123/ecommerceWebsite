from django.shortcuts import render
from django.http import HttpResponse
from.models import Specialday

# Create your views here.
def index(request):
    
    spcl = Specialday.objects.all()
    
    
    return render(request,'index.html',{'spcl':spcl})
   