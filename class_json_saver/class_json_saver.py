import json
from vacancy.vacancy import Vacancy
import pickle


class JsonSaver:
    """
    Класс для сохранения и чтение в файл json экземпляры класса Vacancy
    ❌	Абстрактный класс для хранения данных от которого наследуется JSONSaver написан
    ❌	Реализована локальная фильтрация и агрегация 
    ❌	Получение списка самых высокооплачиваемых вакансий реализовано
    ❌	Класс локального хранения работает с экземплярами классов, а не со списком словарей
    ❌	Фильтрация по вакансиям написана
    ❌	В классе код поиска и код чтения файла вынесены в отдельные методы
    ❌	В классе код удаления и код чтения записи вынесены в отдельные методы
    ❌	Реализован метод проверки корректности файла
    """

    def __init__(self, filename):
        self.__filename = filename

    @property
    def filename(self):
        return self.__filename

    def add_vacancy(self):
        """
        Сохраняет в файл объекты класса Vacancy, преобразовав их в словарь для записи в json
        """
        with open(f"{self.__filename}.json", 'w', encoding='utf-8') as file:
            list_dict = []
            for i in Vacancy.vacancy_list:
                list_dict.append(i.format_to_dict())
            json.dump(list_dict, file, ensure_ascii=False, indent="")

    def import_from_file(self):
        """
        Считывает данные с файла и обратно преобразовывает в обьекты класса Vacancy
        """
        with open(f"{self.__filename}.json", 'r', encoding='utf-8') as file:
            data = file.read()
            list_dict = json.loads(data)
            for i in list_dict:
                Vacancy.reformat_from_dict(i)



