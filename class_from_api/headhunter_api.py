from abs_class.abs_class_api import ApiVacancy
import json
import requests
import time
import csv


class HeadHunter(ApiVacancy):
    """
    Класс для получения и сохранения в csv-файл данных с сервиса hh
    """

    def __init__(self, text):
        self.text = text

list_data_dict = []

for i in range(1, 10):
    page = i
    param = {'text': 'Python',  # Переданное значение ищется в полях вакансии, указанных в параметре search_field
             'area': 1,  # Регион. Необходимо передавать id из справочника /areas. Возможно указание нескольких значений.
             'page': page,  # Параметры пагинации. Параметр per_page ограничен значением в 100
             'per_page': 100  # Параметры пагинации. Параметр per_page ограничен значением в 100. Количество в странице
             }
    req = requests.get("https://api.hh.ru/vacancies", param)  # Посылаем запрос к API
    data = req.content.decode()  # декодируем ответ чтобы  Кириллица отображалось корректно
    data_dict = json.loads(data)
    list_data_dict.extend(data_dict['items'])
    time.sleep(0.25)

data_from_csv_list = []
print(len(list_data_dict))
for i in range(0, len(list_data_dict)):
    items = {}
    items["name"] = list_data_dict[i]["name"].translate(str.maketrans({"\u200e": ''}))
    items["url"] = list_data_dict[i]["alternate_url"]
    if list_data_dict[i]["salary"] is not None:
        items["salary"] = list_data_dict[i]["salary"]["from"]
    items["id"] = list_data_dict[i]["id"]
    data_from_csv_list.append(items)
print(len(data_from_csv_list))
keys = ['name', 'url', 'salary', 'id']
with open('names.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keys)
    writer.writeheader()
    for i in range(0, len(data_from_csv_list)):
        writer.writerow(data_from_csv_list[i])
