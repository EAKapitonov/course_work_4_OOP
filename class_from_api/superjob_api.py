import os
import pprint
from abs_class.abs_class_api import ApiVacancy
import json
import requests
import time
import csv
from vacancy.vacancy import Vacancy


class SuperJobApi(ApiVacancy):
    """
    Класс для работы с API SuperJob
    """
    api_key = os.environ.get('superjob_api_key')
    key = {'X-Api-App-Id': api_key}

    def __init__(self, *args):
        print(SuperJobApi.key)
        self.param = {'keywords': args,  # Переданное значение ищется в полях вакансии, указанных в параметре search_field
                      'page': 2,  # Параметры пагинации. Параметр per_page ограничен значением в 100
                      'count': 100  # Параметры пагинации. Параметр per_page ограничен значением в 100. Количество в странице
                      }
                      # 'parent_id': self.parent_area,  # Код страны.
        self.list_data_dict = []

    def write_to_csv(self):
        """
        Обязывает реализовать методы для добавления вакансий в csv-файл
        """
        pass

    def import_vacancy_from_api(self):
        """
        Метод получения данных через API по указанным параметрам
        """
        print(1)
        req = requests.get("https://api.superjob.ru/2.0/vacancies", headers=SuperJobApi.key, params=self.param)
        print(2)
        data = req.content.decode()  # декодируем ответ чтобы Кириллица отображалось корректно
        data_dict = json.loads(data)
        self.list_data_dict.extend(data_dict['objects'])
        print(len(data_dict['objects']))
        pprint.pprint(self.list_data_dict[5])

    def add_to_vacancy(self) -> None:
        """
        Метод добавляет данные в класс Вакансии
        """
        pass

    def import_vacanсy_from_csv(self, url_file):
        """
        Метод считывает ранее записанные данные в файл csv и
        добавляет данные в класс Vacancy
        :return:
        """
        pass


qw = SuperJobApi("учитель")
qw.import_vacancy_from_api()
