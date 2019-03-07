def weather_get(apikey, city):
  r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={},canada&APPID={}'.format(city, apikey))
  return(r.json())
