from abc import ABC, abstractmethod


class ApiVacancy(ABC):
    """
    Абстрактный класс для работы с Api сервисов по поиску работы
    """

    @abstractmethod
    def import_vacancy_from_api(self):
        """
        Обязывает реализовать метод для импорта данных с сервера
        """
        pass
