import pytest
from class_from_api.superjob_api import SuperJobApi
from vacancy.vacancy import Vacancy


@pytest.fixture
def sj_1():
    sj_1 = SuperJobApi("россия", "учитель")
    sj_1.import_vacanсy_from_csv("superjob_vacancy_1.csv")  # файл superjob_vacancy_1.csv создан специально для тестов
    return sj_1


def test_write_to_csv(sj_1):
    sj_1.write_to_csv()  # должен появится или быть переписан файл superjob_vacancy.csv в папке тестов
    assert len(sj_1.data_from_csv_list) == 0
    assert len(Vacancy.vacancy_list) == 500


def test_import_vacancy_from_csv(sj_1):
    assert len(sj_1.data_from_csv_list) == 0
    assert len(Vacancy.vacancy_list) == 1000


def test_add_to_vacancy(sj_1):
    sj_1.add_to_vacancy()
    assert len(Vacancy.vacancy_list) == 1500


def test_import_vacancy_from_api(sj_1):
    sj_1.import_vacancy_from_api()
    assert len(sj_1.data_from_csv_list) == 500
    assert len(Vacancy.vacancy_list) == 2000
