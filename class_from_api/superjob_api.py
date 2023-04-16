import os
from abs_class.abs_class_api import ApiVacancy
import json
import requests
import csv
from vacancy.vacancy import Vacancy


class SuperJobApi(ApiVacancy):
    """
    Класс для работы с API SuperJob
    """
    api_key = os.environ.get('superjob_api_key')
    key = {'X-Api-App-Id': api_key}

    def __init__(self, country,  *args):
        req_countries = requests.get("https://api.superjob.ru/2.0/countries/")  # запрос списка стран с id
        data_countries = req_countries.content.decode()  # декодируем ответ чтобы Кириллица отображалось корректно
        list_countries = json.loads(data_countries)['objects']
        for i in range(0, len(list_countries)):
            if list_countries[i]["title"] == country.capitalize():
                self.country_id = list_countries[i]["id"]  # сохраняем id указанной страны
                break
        self.args = args
        self.list_data_dict = []
        self.data_from_csv_list = []
        self.param = {}

    def write_to_csv(self):
        """
        Метод записывает данные с API в файл CSV
        :return:
        """
        keys = ['name', 'url', 'salary', 'id_vacancy', 'employer', 'employer_url', 'requirement', 'responsibility']
        with open(f'superjob_vacancy.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for i in range(0, len(self.data_from_csv_list)):
                writer.writerow(self.data_from_csv_list[i])

    def import_vacancy_from_api(self):
        """
        Метод получения данных через API по указанным параметрам
        """
        for i in range(1, 6):
            self.param = {'keywords': self.args,
                          # Переданное значение ищется в полях вакансии, указанных в параметре search_field
                          'page': i,  # Параметры пагинации. Параметр per_page ограничен значением в 100
                          'count': 100,
                          # Параметры пагинации. Параметр per_page ограничен значением в 100. Количество в странице
                          'c': self.country_id  # Код страны.
                          }
            req = requests.get("https://api.superjob.ru/2.0/vacancies", headers=SuperJobApi.key, params=self.param)
            data = req.content.decode()  # декодируем ответ чтобы Кириллица отображалось корректно
            data_dict = json.loads(data)
            self.list_data_dict.extend(data_dict['objects'])  # сохраняем ответ API 1000 вакансий результатов поиска

        for i in range(0, len(self.list_data_dict)):
            items = {}
            items["name"] = self.list_data_dict[i]["profession"]
            items["url"] = self.list_data_dict[i]["link"]
            if self.list_data_dict[i]["payment_from"] is not None:
                items["salary"] = self.list_data_dict[i]["payment_from"]
            else:
                items["salary"] = "Не указан"
            items["id_vacancy"] = self.list_data_dict[i]["id"]
            if "emlopyer" in self.list_data_dict[i].keys():
                items["employer"] = self.list_data_dict[i]["client"]["title"]  # сохранение имени работодателя
                items["employer_url"] = self.list_data_dict[i]["client"]["link"]  # сохранение ссылки на карточку работодателя
            else:
                items["employer"] = "нет данных"  # сохранение имени работодателя
                items["employer_url"] = "нет данных"  # сохранение ссылки на карточку работодателя
            items["requirement"] = self.list_data_dict[i]['candidat']  # сохранение требований к вакансии
            items["responsibility"] = self.list_data_dict[i]['vacancyRichText']  # сохранение обязанностей вакансии
            self.data_from_csv_list.append(items)

    def add_to_vacancy(self) -> None:
        """
        Метод добавляет данные в класс Вакансии
        """
        for i in range(0, len(self.data_from_csv_list)):
            Vacancy(self.data_from_csv_list[i]['name'], self.data_from_csv_list[i]['url'],
                    self.data_from_csv_list[i]['salary'], self.data_from_csv_list[i]['id_vacancy'],
                    self.data_from_csv_list[i]['employer'], self.data_from_csv_list[i]['employer_url'],
                    self.data_from_csv_list[i]['requirement'], self.data_from_csv_list[i]['responsibility'])

    def import_vacanсy_from_csv(self, url_file="../class_from_api/superjob_vacancy.csv"):
        """
        Метод считывает ранее записанные данные в файл csv и
        добавляет данные в класс Vacancy
        :return:
        """
        with open(url_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            print(2)
            for i in reader:
                Vacancy(i['name'], i['url'],
                        i['salary'], i['id_vacancy'],
                        i['employer'], i['employer_url'],
                        i['requirement'], i['responsibility'])

