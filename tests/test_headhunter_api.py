import pytest
from class_from_api.headhunter_api import HeadHunter
from vacancy.vacancy import Vacancy


@pytest.fixture
def headhunter_1():
    headhunter_1 = HeadHunter("россия", "учитель")
    headhunter_1.import_vacanсy_from_csv("vacancy_1.csv")  # файл vacancy_1.csv создан специально для тестов
    return headhunter_1

def test_write_to_csv(headhunter_1):
    headhunter_1.write_to_csv()  # должен появится или быть переписан файл vacancy.csv в папке тестов
    assert len(headhunter_1.data_from_csv_list) == 0
    assert len(Vacancy.vacancy_list) == 1000

def test_import_vacancy_from_csv(headhunter_1):
    assert len(headhunter_1.data_from_csv_list) == 0
    assert len(Vacancy.vacancy_list) == 2000


def test_add_to_vacancy(headhunter_1):
    headhunter_1.add_to_vacancy()
    assert len(Vacancy.vacancy_list) == 3000


def test_import_vacancy_from_api(headhunter_1):
    headhunter_1.import_vacancy_from_api()
    assert len(headhunter_1.data_from_csv_list) == 1000
    assert len(Vacancy.vacancy_list) == 4000
