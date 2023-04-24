import pytest
from class_json_saver.class_json_saver import JsonSaver


@pytest.fixture
def json_saver():
    json_test = JsonSaver("json_test")
    json_test.import_from_file()
    return json_test


def test_add_vacancy(json_saver):
    assert len(json_saver.vacancy_list) == 1352
    assert json_saver.top_salary()[0].salary == 4500000000000000000000000000


def test_search_vacancy(json_saver):
    assert json_saver.search_vacancy("Утка для поиска")[0].id_vacancy == 79331303
    assert json_saver.search_vacancy("Утка для поиска")[1].id_vacancy == 79635316
    assert json_saver.search_vacancy("Утка для поиска")[2].id_vacancy == 78901679


def test_check_file(json_saver):
    assert json_saver.check_file() == "Файл корректный"
