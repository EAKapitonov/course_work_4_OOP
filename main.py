from class_from_api.superjob_api import SuperJobApi
from class_from_api.headhunter_api import HeadHunter
from vacancy.vacancy import Vacancy
from class_json_saver.class_json_saver import JsonSaver

print("Здравствуйте. Введите ключевое слово для поиска")
text = input()
print("Введите страну где искать вакансии")
country = input()
hh = HeadHunter(country, text)  # создаем объект класса HeadHunter с параметрами поиска
sj = SuperJobApi(country, text)  # создаем объект класса SuperJobApi с параметрами поиска
hh.import_vacancy_from_api()  # импортируем данные с API HeadHunter
print("Импорт с HH завершено удачно")
sj.import_vacancy_from_api()  # импортируем данные с API SuperJobApi
print("Импорт с SJ завершено удачно")
hh.response_format()
sj.response_format()
hh.add_to_vacancy()  # создаем объекты класса Vacancy
print(len(Vacancy.vacancy_list))  # Проверяем создание объектов класса Vacancy, выдоим общее количество
sj.add_to_vacancy()  # создаем объекты класса Vacancy
print(len(Vacancy.vacancy_list))  # Проверяем создание объектов класса Vacancy, выдоим общее количество
jso = JsonSaver("Jso")
jso.add_vacancy()

"""jso = JsonSaver("Jso")
jso.import_from_file()"""
