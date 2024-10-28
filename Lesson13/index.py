from downloader.downloader import Weather
from config.config import INPUT_FILE, OUTPUT_FILE


weather_list = []
weather = Weather()
city_list = weather.get_data_from_yaml(INPUT_FILE)

if city_list:
    for city in city_list:
        weather_list.append(weather.get_weather(city))

    weather.save_to_csv(OUTPUT_FILE, weather_list)