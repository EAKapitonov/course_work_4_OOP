from abc import ABC, abstractmethod

class ApiVacancy(ABC):
    """
    Абстрактный класс для работы с Api сервисов по поиску работы
    """
    @abstractmethod
    def add_to_csv(self):
        """
        Обязывает реализовать методы для добавления вакансий в csv-файл
        """
        pass

