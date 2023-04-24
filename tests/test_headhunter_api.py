import pytest
from class_from_api.headhunter_api import HeadHunter


@pytest.fixture
def headhunter_1():
    headhunter_1 = HeadHunter("россия", "учитель")
    return headhunter_1


def test_import_vacancy_from_api(headhunter_1):
    headhunter_1.import_vacancy_from_api()
    assert len(headhunter_1.list_data_dict) == 1000
    headhunter_1.response_format()
    assert len(headhunter_1.data_from_vacancy[0]) == 8

