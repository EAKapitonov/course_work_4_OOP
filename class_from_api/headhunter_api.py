from abs_class.abs_class_api import ApiVacancy
import json
import requests
import time


class HeadHunter(ApiVacancy):
    """
    Класс для получения и сохранения в csv-файл данных с сервиса hh
    """

    def __init__(self, text):
        self.text = text


list_data_dict = []
page = 2
param = {'text': 'Python',  # Переданное значение ищется в полях вакансии, указанных в параметре search_field
         'area': 1,  # Регион. Необходимо передавать id из справочника /areas. Возможно указание нескольких значений.
         'page': page,  # Параметры пагинации. Параметр per_page ограничен значением в 100
         'per_page': 100  # Параметры пагинации. Параметр per_page ограничен значением в 100. Количество в странице
         }
req = requests.get("https://api.hh.ru/vacancies", param)  # Посылаем запрос к API
data = req.content.decode()  # декодируем ответ чтобы  Кириллица отображалось корректно
data_dict = json.loads(data)
list_data_dict.extend(data_dict['items'])
print(data_dict['items'][0])
print("все собрано")
