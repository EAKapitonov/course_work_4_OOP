from abc import ABC, abstractmethod

class Vacancy_abc(ABC):
    """
    Абстрактный класс для работы с вакансиями
    """

    @abstractmethod
    def a(self):
        """

        :return:
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

