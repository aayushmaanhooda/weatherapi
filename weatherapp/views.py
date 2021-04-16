from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    city = request.GET.get('city' , 'delhi')
    url= f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=5a24b4e93e43f2fa556ce50833f7a41c'
    data = requests.get(url).json()
    payload = {'city':data['name'] ,
                'weather':data['weather'][0]['main'],
                 'icon':data['weather'][0]['icon'],
                'kelvin_temprature':data['main']['temp'] ,
                'celcius_temprature':int(data['main']['temp'] -273),
                 'pressure': data['main']['pressure'] , 
                 'humidity':data['main']['humidity'],
                 'description': data['weather'][0]['description'],
                 
                  }
    context = {
        'data': payload
    }
    print(context)
    return render(request , 'home.html' , context)