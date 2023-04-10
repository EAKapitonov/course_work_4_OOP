from abc import ABC, abstractmethod

class Vacancy(ABC):
    """
    Абстрактный класс для работы с вакансиями
    """
    @abstractmethod
    def add_to_csv(self):
        """
        Обязывает реализовать методы для добавления вакансий в csv-файл
        """
        pass

    @abstractmethod
    def import_vacancy_from_csv(self):
        """
        Получения данных из csv-файла по указанным критериям.
        """
        pass

    @abstractmethod
    def remove_vacancy_from_csv(self):
        """
        Удаления информации о вакансии из файла
        """
        pass