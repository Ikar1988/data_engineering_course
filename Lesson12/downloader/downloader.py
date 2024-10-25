import requests
import xml.etree.ElementTree as ET
import pandas as pd
import yaml

class Downloader:

    def get_data_from_yaml(self, file):
        with open(file, "r") as f:
            filedata = yaml.load(f, Loader=yaml.FullLoader)
            return list(filedata)


    def save_to_csv(self, file, data):
        df = pd.DataFrame(data)
        df.to_csv(file, index=False)


class Currency(Downloader):

    def get_currency(self, date, currency_name='USD'):
        url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}'

        response = requests.get(url)

        if response.status_code == 200:
            root_node = ET.fromstring(response.text)
            for tag in root_node.findall('Valute'):

                currency = tag.find('CharCode').text
                if currency == currency_name:
                    value = tag.find('Value').text
                    return {'date': date, 'currency': currency, 'value': value}
        else:
            return False


class Weather(Downloader):

    access_key = 'ba39f67255e4875e3b53e38d0a8c5e5b'

    def get_weather(self, location):
        url = f'https://api.weatherstack.com/current?access_key={self.access_key}&query={location}&format=json'
        response = requests.get(url).json()
        return {
            'city': location,
            'temperature': response['current']['temperature']
        }