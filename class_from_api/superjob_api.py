import os

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

    def __init__(self,text, ):
        self.param = {'keyword': text,  # Переданное значение ищется в полях вакансии, указанных в параметре search_field
                     # 'parent_id': self.parent_area,  # Код страны.
                     # 'page': page,  # Параметры пагинации. Параметр per_page ограничен значением в 100
                     # 'per_page': 100  # Параметры пагинации. Параметр per_page ограничен значением в 100. Количество в странице
                     }



    def write_to_csv(self):
        """
        Обязывает реализовать методы для добавления вакансий в csv-файл
        """
        pass

    def import_vacancy_from_api(self):
        """
        Метод получения данных через API по указанным параметрам
        """
        req = requests.get("https://api.hh.ru/vacancies",headers=SuperJobApi.key, params=self.param)
        pass

    def add_to_vacancy(self) -> None:
        """
        Метод добавляет данные в класс Вакансии
        """
        pass

    def import_vacansy_from_csv(self, url_file):
        """
        Метод считывает ранее записанные данные в файл csv и
        добавляет данные в класс Vacancy
        :return:
        """
        pass


