geo_s ='https://maps.googleapis.com/maps/api/geocode/json'
param = {'address': address, 'key': 'YOUR_KEY'}
response = requests.get(geo_s, params=param)
json_dict = response.json()
lat = json_dict['results'][0]['geometry']['location']['lat']
lng = json_dict['results'][0]['geometry']['location']['lng']
print({'lat': lat, 'lng': lng})
