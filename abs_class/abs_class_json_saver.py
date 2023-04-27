from abc import ABC, abstractmethod
from class_from_api.headhunter_api import HeadHunter
from class_from_api.superjob_api import SuperJobApi


class JsonSaverAbs(ABC):
    """
    Абстрактный класс для работы с данными полученными с api     
    """

    @abstractmethod
    def save_vacancies(self):
        """
        Сохраняет в файл объекты класса Vacancy, преобразовав их в словарь для записи в json
        """
        pass

    @abstractmethod
    def import_from_file(self):
        """
        Считывает данные с файла и обратно преобразовывает в обьекты класса Vacancy
        """
        pass

    @abstractmethod
    def top_salary(self):
        """
        Возвращает список из ТОП-5 самых высокооплачиваемых вакансий реализовано
        """
        pass

    @abstractmethod
    def import_from_api(self, headhunter: HeadHunter, superjob: SuperJobApi):
        """
        Импортирует вакансии с Api и создает объекты класса Vacancy
        """
        pass
