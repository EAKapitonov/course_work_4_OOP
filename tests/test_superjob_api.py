import pytest
from class_from_api.superjob_api import SuperJobApi


@pytest.fixture
def superjob_1():
    superjob_1 = SuperJobApi("россия", "учитель")
    return superjob_1


def test_import_vacancy_from_api(superjob_1):
    superjob_1.import_vacancy_from_api()
    assert len(superjob_1.list_data_dict) == 500
    superjob_1.response_format()
    assert len(superjob_1.data_from_vacancy[0]) == 8
