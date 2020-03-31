from django.shortcuts import render
from .models import Destination


# Create your views here.
def home(request):
    dest1= Destination()
    dest1.name = 'Lahore'
    dest1.desc = 'The city or kings'
    dest1.img= 'destination_1.jpg'
    dest1.price= 3275
    dest1.offer= False
    
    dest2=Destination()
    dest2.name='Faisalabad'
    dest2.desc='Manchester of pakistan'
    dest2.img = 'destination_2.jpg'
    dest2.price=248
    dest2.offer= True

    dest3=Destination()
    dest3.name='Karachi'
    dest3.desc='The city of lights'
    dest3.img= 'destination_3.jpg'
    dest3.price= 2020
    dest3.offer= False

    dests = [dest1,dest2,dest3]


    return render(request, 'index.html', {'dests':dests})


