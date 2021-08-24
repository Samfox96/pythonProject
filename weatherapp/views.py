from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Sydney'


    appid = '1aaee726417c90d6a16ba8d49ecb7d8c'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    lat = res['coord']['lat']
    lon = res['coord']['lon']
    min = res['main']['temp_min']
    max = res['main']['temp_max']
    hum = res['main']['humidity']
    day= datetime.date.today()

    return render(request, 'Weather.html', {'description': description, 'icon': icon, 'temp': temp,
                                            'day': day, 'city': city, 'lat': lat, 'lon': lon, 'min': min,
                                            'max': max, 'hum': hum}

                  )