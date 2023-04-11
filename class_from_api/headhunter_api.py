from abs_class.abs_class_api import ApiVacancy
import json
import requests
import time
import csv
from vacancy.vacancy import Vacancy


class HeadHunter(ApiVacancy):
    """
    Класс для работы с API HH
    """

    def __init__(self, text, parent_area):
        """
        Инициализация объекта класса параметрами поиска вакансии
        """
        self.text = text  # Текст поиска вакансии
        self.parent_area = None
        req = requests.get("https://api.hh.ru/areas/countries")
        data_country = req.content.decode()  # декодируем ответ чтобы  Кириллица отображалось корректно
        data_dict_country = json.loads(data_country)
        for i in range(0, len(data_dict_country)):
            if data_dict_country[i]["name"] == parent_area.capitalize():
                self.parent_area = int(data_dict_country[i]["id"])  # сохранение в атрибут id указанной страны
                break
        if self.parent_area is None:  # Проверяем найдено-ли указанная страна
            print("Указанная страна не найдено, введите другую страну")
            arent_area = input()
            self.__init__(text, parent_area)


    def import_vacancy(self):
        """
        Метод получения данных через API по указанным параметрам
        """
        list_data_dict = []
        for i in range(1, 11):
            page = i
            param = {'text': self.text,  # Переданное значение ищется в полях вакансии, указанных в параметре search_field
                     'parent_id': self.parent_area,  # Код страны.
                     'page': page,  # Параметры пагинации. Параметр per_page ограничен значением в 100
                     'per_page': 100  # Параметры пагинации. Параметр per_page ограничен значением в 100. Количество в странице
                     }
            req = requests.get("https://api.hh.ru/vacancies", param)  # Посылаем запрос к API
            data = req.content.decode()  # декодируем ответ чтобы  Кириллица отображалось корректно
            data_dict = json.loads(data)
            list_data_dict.extend(data_dict['items'])
            time.sleep(0.25)
        data_from_csv_list = []
        items = {}
        for i in range(0, len(list_data_dict)):
            items["name"] = list_data_dict[i]["name"].translate(str.maketrans({"\u200e": ''}))
            items["url"] = list_data_dict[i]["alternate_url"]
            if list_data_dict[i]["salary"] is not None:
                items["salary"] = list_data_dict[i]["salary"]["from"]
            else:
                items["salary"] = "Не указан"
            items["id_vacancy"] = list_data_dict[i]["id"]
            items["employer"]      делаю тут
            items["employer_url"]
            data_from_csv_list.append(items)
        keys = ['name', 'url', 'salary', 'id_vacancy', 'employer', 'employer_url', 'requirement', 'responsibility']
        with open('names.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for i in range(0, len(data_from_csv_list)):
                writer.writerow(data_from_csv_list[i])


name, url, salary, id_vacancy, employer, employer_url, requirement, responsibility




