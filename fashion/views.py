from django.shortcuts import render
from django.http import HttpResponse
from.models import Specialday

# Create your views here.
def index(request):
    spcl1 = Specialday()
    spcl1.catagory = 'Women'
    spcl1.day_name = 'Year End Sale'
    spcl1.desc ='Now started year end sale with flat 50%'
    spcl1.img = 'hero-1.jpg'
    spcl1.sale = True
    
    spcl2 = Specialday()
    spcl2.catagory = 'Kids'
    spcl2.day_name = 'Year End Sale'
    spcl2.desc ='Now started year end sale with flat 50%'
    spcl2.img = 'hero-2.jpg'
    spcl2.sale = True

    spcl3 = Specialday()
    spcl3.catagory = 'Men'
    spcl3.day_name = 'Year End Sale'
    spcl3.desc ='Now started year end sale with flat 50%'
    spcl3.img = 'hero-2.jpg'
    spcl3.sale = False
    
    spcl = [spcl1,spcl2,spcl3]
    
    
    return render(request,'index.html',{'spcl':spcl})
   