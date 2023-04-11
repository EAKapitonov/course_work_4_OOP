from abs_class import abs_class_vacancy


class Vacancy(abs_class_vacancy):
    """
    Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название
    вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т.п. (не менее четырех) Класс должен
    поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные, которыми инициализируются
    его атрибуты.

    """
    def __init__(self, name, url, salary, id_vacancy, employer, employer_url, requirement, responsibility):
        self.name = name  # название вакансии
        self.url = url  # ссылка на  вакансию
        self.salary = salary  # объявленная зарплата
        self.id_vacancy = id_vacancy  # id вакансии
        self.employer = employer  # Название фирмы работодателя
        self.employer_url = employer_url  # ссылка на карточку работодателя
        self.requirement = requirement  # требования вакансии к работнику
        self.responsibility = responsibility  # обязанности должности


