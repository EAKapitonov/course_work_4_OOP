from abc import ABC, abstractmethod


class VacancyABC(ABC):
    """
    Абстрактный класс для работы с вакансиями
    """

    @abstractmethod
    def name(self):
        """
        Обязывает создать свойство name
        """
        pass

    @abstractmethod
    def url(self):
        """
        Обязывает создать свойство url
        """
        pass

    @abstractmethod
    def salary(self):
        """
        Обязывает создать свойство salary
        """
        pass

    @abstractmethod
    def id_vacancy(self):
        """
        Обязывает создать свойство id_vacancy
        """
        pass

    @abstractmethod
    def employer(self):
        """
        Обязывает создать свойство employer
        """
        pass

    @abstractmethod
    def requirement(self):
        """
        Обязывает создать свойство requirement
        """
        pass

    @abstractmethod
    def employer_url(self):
        """
        Обязывает создать свойство employer_url
        """
        pass

    @abstractmethod
    def responsibility(self):
        """
        Обязывает создать свойство responsibility
        """
        pass
