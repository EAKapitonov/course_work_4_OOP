from abs_class.abs_class_api import ApiVacancy
import json
import requests
import time
from vacancy.vacancy import Vacancy


class HeadHunter(ApiVacancy):
    """
    Класс для работы с API HH
    """

    def __init__(self, parent_area, text):
        """
        Инициализация объекта класса параметрами поиска вакансии
        """
        self.text = text  # Текст поиска вакансии
        self.parent_area = None
        self.parent_area = self.requests_list_id_country(parent_area, text)
        self.list_data_dict = []
        self.data_from_vacancy = []

    def requests_list_id_country(self, parent_area, text):
        """
        Получение списка стран
        """
        req = requests.get("https://api.hh.ru/areas/countries")
        data_country = req.content.decode()  # декодируем ответ чтобы Кириллица отображалось корректно
        data_dict_country = json.loads(data_country)
        for i in range(0, len(data_dict_country)):
            if data_dict_country[i]["name"] == parent_area.capitalize():
                return int(data_dict_country[i]["id"])  # сохранение в атрибут id указанной страны
        if self.parent_area is None:  # Проверяем найдено-ли указанная страна
            ValueError

    def import_vacancy_from_api(self):
        """
        Метод получения данных через API по указанным параметрам
        """
        try:
            list_data_dict = []
            for i in range(1, 2):
                page = i
                param = {'text': self.text,
                         # Переданное значение ищется в полях вакансии, указанных в параметре search_field
                         'parent_id': self.parent_area,  # Код страны.
                         'page': page,  # Параметры пагинации. Параметр per_page ограничен значением в 100
                         'per_page': 100
                         # Параметры пагинации. Параметр per_page ограничен значением в 100. Количество в странице
                         }
                req = requests.get("https://api.hh.ru/vacancies", param)  # Посылаем запрос к API
                data = req.content.decode()  # декодируем ответ чтобы  Кириллица отображалось корректно
                data_dict = json.loads(data)
                self.list_data_dict.extend(data_dict['items'])
                time.sleep(0.25)
        except ValueError:
            print("Ошибка")

    def response_format(self):
        """
        Форматирования ответа сервера
        """
        for i in range(0, len(self.list_data_dict)):
            items = {}
            items["name"] = self.list_data_dict[i]["name"]
            items["url"] = self.list_data_dict[i]["alternate_url"]
            if isinstance(self.list_data_dict[i]["salary"], int):
                items["salary"] = self.list_data_dict[i]["salary"]["from"]
            else:
                items["salary"] = 0
            items["id_vacancy"] = self.list_data_dict[i]["id"]
            if "emlopyer" in self.list_data_dict[i].keys():
                items["employer"] = self.list_data_dict[i]["emlopyer"]["name"]  # сохранение имени работодателя
                items["employer_url"] = self.list_data_dict[i]["emlopyer"][
                    "alternate_url"]  # сохранение ссылки на карточку работодателя
            else:
                items["employer"] = "нет данных"  # сохранение имени работодателя
                items["employer_url"] = "нет данных"  # сохранение ссылки на карточку работодателя
            items["requirement"] = self.list_data_dict[i]['snippet']['requirement']  # сохранение требований к вакансии
            items["responsibility"] = self.list_data_dict[i]['snippet'][
                'responsibility']  # сохранение обязанностей вакансии
            self.data_from_vacancy.append(items)


    def add_to_vacancy(self) -> None:
        """
        Метод добавляет данные в класс Вакансии
        """
        for i in range(0, len(self.data_from_vacancy)):
            Vacancy(self.data_from_vacancy[i]['name'], self.data_from_vacancy[i]['url'],
                    self.data_from_vacancy[i]['salary'], self.data_from_vacancy[i]['id_vacancy'],
                    self.data_from_vacancy[i]['employer'], self.data_from_vacancy[i]['employer_url'],
                    self.data_from_vacancy[i]['requirement'], self.data_from_vacancy[i]['responsibility'])
