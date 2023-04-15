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
        self.data_from_csv_list = []

    def import_vacancy_from_api(self):
        """
        Метод получения данных через API по указанным параметрам
        """
        list_data_dict = []
        for i in range(1, 11):
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
            list_data_dict.extend(data_dict['items'])
            time.sleep(0.25)
        print(len(list_data_dict))
        for i in range(0, len(list_data_dict)):
            items = {}
            items["name"] = list_data_dict[i]["name"].translate(str.maketrans({"\u200e": ''}))
            items["url"] = list_data_dict[i]["alternate_url"]
            if list_data_dict[i]["salary"] is not None:
                items["salary"] = list_data_dict[i]["salary"]["from"]
            else:
                items["salary"] = "Не указан"
            items["id_vacancy"] = list_data_dict[i]["id"]
            if "emlopyer" in list_data_dict[i].keys():
                items["employer"] = list_data_dict[i]["emlopyer"]["name"]  # сохранение имени работодателя
                items["employer_url"] = list_data_dict[i]["emlopyer"][
                    "alternate_url"]  # сохранение ссылки на карточку работодателя
            else:
                items["employer"] = "нет данных"  # сохранение имени работодателя
                items["employer_url"] = "нет данных"  # сохранение ссылки на карточку работодателя
            items["requirement"] = list_data_dict[i]['snippet']['requirement']  # сохранение требований к вакансии
            items["responsibility"] = list_data_dict[i]['snippet']['responsibility']  # сохранение обязанностей вакансии
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

    def write_to_csv(self):
        """
        Метод записывает данные с API в файл CSV
        :return:
        """
        keys = ['name', 'url', 'salary', 'id_vacancy', 'employer', 'employer_url', 'requirement', 'responsibility']
        with open(f'vacancy.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for i in range(0, len(self.data_from_csv_list)):
                writer.writerow(self.data_from_csv_list[i])

    def import_vacanсy_from_csv(self, url_file):
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


gt = HeadHunter('учитель', 'россия')
print(1)
# gt.import_vacancy_from_api()
# gt.write_to_csv()
# print(3)
gt.import_vacanсy_from_csv("../class_from_api/vacancy.csv")
gt.add_to_vacancy()
print(Vacancy.vacancy_list[1].name)
print(Vacancy.vacancy_list[1] < Vacancy.vacancy_list[2])
print(len(Vacancy.vacancy_list))
