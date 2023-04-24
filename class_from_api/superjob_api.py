import os
import sys
from abs_class.abs_class_api import ApiVacancy
import json
import requests


class SuperJobApi(ApiVacancy):
    """
    Класс для работы с API SuperJob
    """
    api_key = os.environ.get('superjob_api_key')
    key = {'X-Api-App-Id': api_key}

    def __init__(self, parent_area, *args):
        self.parent_area = None
        self.parent_area = self.requests_list_id_country(parent_area, *args)
        self.args = args
        self.list_data_dict = []
        self.data_from_vacancy = []

    def requests_list_id_country(self, parent_area, *args):
        """
        Получение списка стран
        """
        req_countries = requests.get("https://api.superjob.ru/2.0/countries/")  # запрос списка стран с id
        data_countries = req_countries.content.decode()  # декодируем ответ чтобы Кириллица отображалось корректно
        list_countries = json.loads(data_countries)['objects']
        for i in range(0, len(list_countries)):
            if list_countries[i]["title"] == parent_area.capitalize():
                return list_countries[i]["id"]  # сохраняем id указанной страны
        if self.parent_area is None:  # Проверяем найдено-ли указанная страна
            print("Указанная страна не найдена, перезагрузите программу и попробуйте снова")
            sys.exit()

    def import_vacancy_from_api(self):
        """
        Метод получения данных через API по указанным параметрам
        """
        try:
            for i in range(1, 6):
                param = {'keywords': self.args,
                         # Переданное значение ищется в полях вакансии, указанных в параметре search_field
                         'page': i,  # Параметры пагинации. Параметр per_page ограничен значением в 100
                         'count': 100,
                         # Параметры пагинации. Параметр per_page ограничен значением в 100. Количество в странице
                         'c': self.parent_area  # Код страны.
                         }
                req = requests.get("https://api.superjob.ru/2.0/vacancies", headers=SuperJobApi.key, params=param)
                data = req.content.decode()  # декодируем ответ чтобы Кириллица отображалось корректно
                data_dict = json.loads(data)
                self.list_data_dict.extend(data_dict['objects'])  # сохраняем ответ API 1000 вакансий результатов поиска
        except ValueError:
            print("Ошибка значения, попробуйте снова")
            sys.exit()

    def response_format(self):
        """
        Форматирования ответа сервера
        """
        for i in range(0, len(self.list_data_dict)):
            items = {}
            items["name"] = self.list_data_dict[i]["profession"]
            items["url"] = self.list_data_dict[i]["link"]
            if isinstance(self.list_data_dict[i]["payment_from"], int):
                items["salary"] = self.list_data_dict[i]["payment_from"]
            else:
                items["salary"] = 0
            items["id_vacancy"] = self.list_data_dict[i]["id"]
            if "firm_name" in self.list_data_dict[i]:
                items["employer"] = self.list_data_dict[i]["firm_name"]  # сохранение имени работодателя
                items["employer_url"] = self.list_data_dict[i]["link"]  # сохранение ссылки на карточку работодателя
            else:
                items["employer"] = "нет данных"  # сохранение имени работодателя
                items["employer_url"] = "нет данных"  # сохранение ссылки на карточку работодателя
            items["requirement"] = self.list_data_dict[i]['candidat']  # сохранение требований к вакансии
            items["responsibility"] = self.list_data_dict[i]['vacancyRichText']  # сохранение обязанностей вакансии
            self.data_from_vacancy.append(items)

    def get_to_vacancy(self):
        """
        Метод возвращает полученные данные с API
        """
        return self.data_from_vacancy
