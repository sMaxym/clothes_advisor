import requests
import pyowm


class Weather:
    def __init__(self, url, apikey):
        self.__url = url
        self.__apikey = apikey
        self.__owm = pyowm.OWM(self.__apikey)

    def get_weather_by_location(self, coords):
        observation = self.__owm.weather_at_coords(coords[0], coords[1])
        weather_data = observation.get_weather()
        return weather_data

    def get_temperature(self, coords):
        weather_data = self.get_weather_by_location(coords)
        temperature = weather_data.get_temperature(unit='celsius')
        return temperature['temp']
