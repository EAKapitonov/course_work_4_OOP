from abc import ABC, abstractmethod

class Vacancy_abc(ABC):
    """
    Абстрактный класс для работы с вакансиями
    """

    @abstractmethod
    @property
    def name(self, ):
        """
        Обязывает создать свойство name
        """
        pass


    @abstractmethod
    @property
    def url(self, ):
        """
        Обязывает создать свойство url
        """
        pass


    @abstractmethod
    @property
    def salary(self, ):
        """
        Обязывает создать свойство salary
        """
        pass


    @abstractmethod
    @property
    def id_vacancy(self, ):
        """
        Обязывает создать свойство id_vacancy
        """
        pass

    @abstractmethod
    @property
    def employer(self, ):
        """
        Обязывает создать свойство employer
        """
        pass

    @abstractmethod
    @property
    def requirement(self, ):
        """
        Обязывает создать свойство requirement
        """
        pass

    @abstractmethod
    @property
    def employer_url(self, ):
        """
        Обязывает создать свойство employer_url
        """
        pass

    @abstractmethod
    @property
    def responsibility(self, ):
        """
        Обязывает создать свойство responsibility
        """
        pass


    def __lt__(self, other):  # определяет поведение оператора сравнения «меньше», <
        if self.salary == "Не указан" or other.salary == "Не указан":
            return "Зарплата не указана"
        if self.salary < other.salary:
            return True
        else:
            return False

    def __le__(self, other):  # определяет поведение оператора сравнения «меньше или равно», <=
        if self.salary == "Не указан" or other.salary == "Не указан":
            return "Зарплата не указана"
        if self.salary <= other.salary:
            return True
        else:
            return False

    def __eq__(self, other):  # определяет поведение оператора «равенства», ==.
        if self.salary == "Не указан" or other.salary == "Не указан":
            return "Зарплата не указана"
        if self.salary == other.salary:
            return True
        else:
            return False

    def __ne__(self, other):  # определяет поведение оператора «неравенства», !=.
        if self.salary == "Не указан" or other.salary == "Не указан":
            return "Зарплата не указана"
        if self.salary != other.salary:
            return True
        else:
            return False

    def __gt__(self, other):  # определяет поведение оператора сравнения «больше», >.
        if self.salary == "Не указан" or other.salary == "Не указан":
            return "Зарплата не указана"
        if self.salary > other.salary:
            return True
        else:
            return False

    def __ge__(self, other):  # определяет поведение оператора сравнения «больше или равно», >=.
        if self.salary == "Не указан" or other.salary == "Не указан":
            return "Зарплата не указана"
        if self.salary >= other.salary:
            return True
        else:
            return False

