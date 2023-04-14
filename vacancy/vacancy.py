from abs_class.abs_class_vacancy import VacancyABC


class Vacancy(VacancyABC):
    """
    Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название
    вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т.п. (не менее четырех) Класс должен
    поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные, которыми инициализируются
    его атрибуты.

    """

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
