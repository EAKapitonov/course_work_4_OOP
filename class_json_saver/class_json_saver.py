import json
import os.path
from vacancy.vacancy import Vacancy
from abs_class.abs_class_json_saver import JsonSaverAbs
from class_from_api.headhunter_api import HeadHunter
from class_from_api.superjob_api import SuperJobApi


class JsonSaver(JsonSaverAbs):
    """
    Класс для сохранения и чтение в файл json экземпляры класса Vacancy
    """

    def __init__(self, filename):
        self.__filename = filename
        self.vacancy_list = []

    @property
    def filename(self):
        return self.__filename

    def save_vacancies(self):
        """
        Сохраняет в файл объекты класса Vacancy, преобразовав их в словарь для записи в json
        """
        with open(f"{self.__filename}.json", 'w', encoding='utf-8') as file:
            list_dict = []
            for i in self.vacancy_list:
                list_dict.append(i.format_to_dict())
            json.dump(list_dict, file, ensure_ascii=False, indent="")

    def import_from_file(self):
        """
        Считывает данные с файла и обратно преобразовывает в объекты класса Vacancy
        """
        with open(f"{self.__filename}.json", 'r', encoding='utf-8') as file:
            data = file.read()
            list_dict = json.loads(data)
            for i in list_dict:
                self.vacancy_list.append(Vacancy.reformat_from_dict(i))

    def import_from_api(self, headhunter: HeadHunter, superjob: SuperJobApi):
        """
        Импортирует вакансии с Api и создает объекты класса Vacancy
        """
        list_1 = headhunter.get_to_vacancy()
        for i in range(0, len(list_1)):
            self.vacancy_list.append(Vacancy(list_1[i]['name'], list_1[i]['url'],
                                             list_1[i]['salary'], list_1[i]['id_vacancy'],
                                             list_1[i]['employer'], list_1[i]['employer_url'],
                                             list_1[i]['requirement'], list_1[i]['responsibility']))
        list_2 = superjob.get_to_vacancy()
        for i in range(0, len(list_2)):
            self.vacancy_list.append(Vacancy(list_2[i]['name'], list_2[i]['url'],
                                             list_2[i]['salary'], list_2[i]['id_vacancy'],
                                             list_2[i]['employer'], list_2[i]['employer_url'],
                                             list_2[i]['requirement'], list_2[i]['responsibility']))

    def top_salary(self):
        """
        Возвращает список из ТОП-5 самых высокооплачиваемых вакансий реализовано
        """
        top_5 = self.vacancy_list
        top_5.sort(key=lambda x: x.salary, reverse=True)
        return top_5[:5]

    def search_vacancy(self, text):
        """
        Ищет указанную строку в названиях, требованиях и обязанностях и выдает список при совпадении
        """
        search_vacancy = []
        for i in self.vacancy_list:
            if text in i.name:
                search_vacancy.append(i)
                continue
            elif i.requirement is not None and text in i.requirement:
                search_vacancy.append(i)
                continue
            elif i.responsibility is not None and text in i.responsibility:
                search_vacancy.append(i)
                continue
        return search_vacancy

    def del_vacancy(self, id_vacancy):
        """
        Удаления из объектов класса Vacancy по указанной id
        """
        x = 0
        for i in self.vacancy_list:
            if id_vacancy == i.id_vacancy:
                self.vacancy_list.pop(x)
                break
            else:
                x = x + 1

    def check_file(self):
        """Проверяет корректность файла"""
        if os.path.isfile(f"{self.__filename}.json"):
            with open(f"{self.__filename}.json", 'r', encoding='utf-8') as file:
                data = file.read()
                list_dict = json.loads(data)
                if isinstance(list_dict, list):
                    if isinstance(list_dict[0], dict):
                        list_key = ['_name', '_url', '_salary', '_id_vacancy', '_employer', '_employer_url',
                                    '_requirement', '_responsibility']
                        for i in list_key:
                            if i not in list_dict[0]:
                                raise ValueError
                        return True
                    else:
                        raise ValueError
                else:
                    raise ValueError
        else:
            raise FileNotFoundError
