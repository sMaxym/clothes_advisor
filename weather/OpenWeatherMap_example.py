# Function get_data_from_URL takes in a URL and parameters
# for an API request and then returns the data (json).

import requests
import pyowm


def get_data_from_URL(base_url, options, APIKEY):
    lat, long = options
    request_url = base_url.format(lat, long, APIKEY)
    r = requests.get(request_url)
    print(r.json())


def get_data_with_wrapper(base_url, options, APIKEY):
    owm = pyowm.OWM(APIKEY)
    observation = owm.weather_at_coords(options[0], options[1])
    w = observation.get_weather()
    print(w.get_temperature(unit='celsius'))


if __name__ == "__main__":
    url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID={}"
    options = (49.824973, 24.176674)
    APIKEY = "160058a98508149e10affb7930083705"
    get_data_with_wrapper(url, options, APIKEY)
