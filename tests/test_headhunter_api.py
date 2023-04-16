import pytest
from class_from_api.headhunter_api import HeadHunter
from vacancy.vacancy import Vacancy


hh = HeadHunter("россия", "учитель")
def test_import_vacancy_from_csv(self):
    hh.import_vacancy_from_csv("../vacancy.csv")
    assert len(hh.data_from_csv_list) == 1000

def test_add_to_vacancy():
    hh.add_to_vacancy()
    assert len(Vacancy.vacancy_list) == 1000

