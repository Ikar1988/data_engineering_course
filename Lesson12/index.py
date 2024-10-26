from downloader.downloader import Currency, Weather


weather_list = []
weather = Weather()
for city in weather.get_data_from_yaml('cities.yaml'):
    weather_list.append(weather.get_weather(city))

weather.save_to_csv('weather.csv', weather_list)


courses = []
currency = Currency()

currency_names = currency.get_data_from_yaml('currencies.yaml')

for day in range(1, 2):
    for currency_name in currency_names:

        if day < 10:
            day_of_november = f'0{str(day)}/11/2023'
            date = f'0{str(day)}.11.2023'
        else:
            day_of_november = f'{str(day)}/11/2023'
            date = f'{str(day)}.11.2023'

        cur = currency.get_currency(day_of_november, currency_name=currency_name)
        if cur:
            courses.append(cur)


currency.save_to_csv('courses.csv', courses)

