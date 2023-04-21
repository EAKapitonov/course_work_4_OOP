from abs_class.abs_class_vacancy import VacancyABC


class Vacancy(VacancyABC):
    """
    Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название
    вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т.п. (не менее четырех) Класс должен
    поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные, которыми инициализируются
    его атрибуты.
   ❌	Инициализатор валидирует добавляемые значения
    """

    __slots__ = ("_name", "_url", "_salary", "_id_vacancy", "_empl",
                 "_employer_url", "_requirement", "_responsibility")
    vacancy_list = []

    def __init__(self, name, url, salary, id_vacancy, empl, employer_url, requirement, responsibility):
        self._name = name  # название вакансии
        self._url = url  # ссылка на  вакансию
        self._salary = salary  # объявленная зарплата
        self._id_vacancy = id_vacancy  # id вакансии
        self._employer = empl  # Название фирмы работодателя
        self._employer_url = employer_url  # ссылка на карточку работодателя
        self._requirement = requirement  # требования вакансии к работнику
        self._responsibility = responsibility  # обязанности должности
        Vacancy.vacancy_list.append(self)

    def __repr__(self):
        return f"Объект класса {self.__class__.__name__}, вакансия -  {self._name}"

    def __str__(self):
        return f"Вакансия {self._name}, с указанной зарплатой {self._salary}, работадатель - {self._employer}"

    def format_to_dict(self) -> dict:
        """Переформатируем экземпляр класса для сохранения в файл"""
        state = {"_name": self._name, "url": self._url, "_salary": self._salary, "_id_vacancy": self._id_vacancy,
                 "_employer": self._employer, "_employer_url": self._employer_url, "_requirement": self._requirement,
                 "_responsibility": self._responsibility}
        return state

    @classmethod
    def reformat_from_dict(cls, state: dict):
        """Восстанавливаем экземпляр класса из файла"""
        cls.__init__(state["_name"],
                     state["url"],
                     int(state["_salary"]),
                     int(state["_id_vacancy"]),
                     state["_employer"],
                     state["_employer_url"],
                     state["_requirement"],
                     state["_responsibility"])

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @property
    def salary(self):
        return self._salary

    @property
    def id_vacancy(self):
        return self._id_vacancy

    @property
    def employer(self):
        return self._employer

    @property
    def employer_url(self):
        return self._employer_url

    @property
    def requirement(self):
        return self.requirement

    @property
    def responsibility(self):
        return self._responsibility

    def __lt__(self, other):  # определяет поведение оператора сравнения «меньше», <
        if self.salary < other.salary:
            return True
        else:
            return False

    def __le__(self, other):  # определяет поведение оператора сравнения «меньше или равно», <=
        if self.salary <= other.salary:
            return True
        else:
            return False

    def __eq__(self, other):  # определяет поведение оператора «равенства», ==.
        if self.salary == other.salary:
            return True
        else:
            return False

    def __ne__(self, other):  # определяет поведение оператора «неравенства», !=.
        if self.salary != other.salary:
            return True
        else:
            return False

    def __gt__(self, other):  # определяет поведение оператора сравнения «больше», >.
        if self.salary > other.salary:
            return True
        else:
            return False

    def __ge__(self, other):  # определяет поведение оператора сравнения «больше или равно», >=.
        if self.salary >= other.salary:
            return True
        else:
            return False
