if __name__ == '__main__':
    manager = WeatherManager(weather_data, wardrobe_data)
    manager.add(WeatherData(new_weather))
    manager.remove(index=2)
    manager.update_wardrobe(new_wardrobe)
    print(manager.sorted(key=lambda x: -x.temp))
    print(manager.proper_clothes(index=1))
