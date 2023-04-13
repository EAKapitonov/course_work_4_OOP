from abs_class.abs_class_vacancy import Vacancy_abc


class Vacancy(Vacancy_abc):
    """
    Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название
    вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т.п. (не менее четырех) Класс должен
    поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные, которыми инициализируются
    его атрибуты.

    """
    vacancy_list = []

    def __init__(self, name, url, salary, id_vacancy, employer, employer_url, requirement, responsibility):
        self._name = name  # название вакансии
        self._url = url  # ссылка на  вакансию
        self._salary = salary  # объявленная зарплата
        self._id_vacancy = id_vacancy  # id вакансии
        self._employer = employer  # Название фирмы работодателя
        self._employer_url = employer_url  # ссылка на карточку работодателя
        self._requirement = requirement  # требования вакансии к работнику
        self._responsibility = responsibility  # обязанности должности
        Vacancy.vacancy_list.append(self)

    @property
    def

