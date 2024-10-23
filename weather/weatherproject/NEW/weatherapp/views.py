from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def home(request):
   
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'indore'     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=edb9f498334c70c9a45a54867a7df2c7
    PARAMS = {'units':'metric'}

              
 data = requests.get(url,params=PARAMS).json()

 description = data['weather'][0]['description']
 icon = data['weather'][0]['icon']
 temp = data['main']['temp']

 day = datetime.date.today()

     return render(request,'weatherapp/index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city })
    
    