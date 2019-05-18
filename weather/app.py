from weather.clothing import Clothing
from weather.weather import Weather
from weather.wardrobe import Wardrobe
import os


def get_clothes(locs):
    clothes = list()
    print(locs)
    with open(os.path.join(os.path.dirname(__file__), 'clothesdata.csv'), 'r') as file:
        line = file.readline()
        for line in file:
            line_data = line.split(',')
            line_data = [item.strip() for item in line_data]
            temperature = line_data[2].split()
            clothes.append(Clothing(line_data[0],
                                    line_data[1],
                                    (int(temperature[0]), int(temperature[1])),
                                    bool(line_data[3]),
                                    int(line_data[4]),
                                    int(line_data[5])))


    url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID={}"
    APIKEY = "160058a98508149e10affb7930083705"

    ward = Wardrobe(*clothes)
    average_tem = 0
    for loc in locs:
        w = Weather(url, APIKEY)
        temp = w.get_temperature(loc)
        average_tem += temp
    average_tem /= len(locs)

    return [el.name for el in ward.get_clothing(average_tem)]


if __name__ == '__main__':
    locs = [(49.817610, 24.023890), (49.848614, 24.037307)]
    print(get_clothes(locs))


