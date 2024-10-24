import requests
import xml.etree.ElementTree as ET
import pandas as pd

courses = []

for day in range(1,31):

    if day < 10:
        day_of_november = f'0{str(day)}/11/2023'
        date = f'0{str(day)}.11.2023'
    else:
        day_of_november = f'{str(day)}/11/2023'
        date = f'{str(day)}.11.2023'

    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={day_of_november}'

    response = requests.get(url)

    if response.status_code == 200:
        root_node = ET.fromstring(response.text)
        for tag in root_node.findall('Valute'):

            currency = tag.find('CharCode').text
            if currency == 'USD':
                value = tag.find('Value').text
                courses.append({'date': date, 'currency': currency, 'value': value})
                print(f'{date}: OK')

    else:
        print('error')

pd = pd.DataFrame(courses)
pd.to_csv('courses.csv')
