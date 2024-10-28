import requests
import xml.etree.ElementTree as ET
import pandas as pd
import yaml
import sys
sys.path.append('..')
from config.config import WEATHER_URL, API_KEY
import logging


class Downloader:

    def __init__(self):
        logging.basicConfig(level=logging.WARNING, filename="base.log", filemode="a",
                            format="%(asctime)s %(levelname)s %(message)s")

    def get_data_from_yaml(self, file):
        try:
            with open(file, "r") as f:
                filedata = yaml.load(f, Loader=yaml.FullLoader)
                return list(filedata)
        except Exception as e:
            logging.error(f'{e}. Файл: {file}')
            print('При открытии YAML файла произошла ошибка. Возможно файл не существует или имеет неизвестный формат')
            # print(e)
            return False

    def save_to_csv(self, file, data):
        df = pd.DataFrame(data)
        df.to_csv(file, index=False)


class Weather(Downloader):

    access_key = API_KEY

    def get_weather(self, location):
        url = f'{WEATHER_URL}?access_key={self.access_key}&query={location}&format=json'
        response = requests.get(url).json()
        return {
            'city': location,
            'temperature': response['current']['temperature']
        }