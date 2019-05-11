from clothing import Clothing
from weather import Weather
from wardrobe import Wardrobe


if __name__ == '__main__':
    clothes = list()
    with open('clothesdata.csv', 'r') as file:
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

    for item in clothes:
        print(item)

    url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID={}"
    APIKEY = "160058a98508149e10affb7930083705"
    locs = [(49.817610, 24.023890), (49.848614, 24.037307)]

    ward = Wardrobe(*clothes)

    for loc in locs:
        w = Weather(url, APIKEY)
        temp = w.get_temperature(loc)
        print(temp, ward.get_clothing(temp))

