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
hh.response_format()
print(f"Импорт с HH завершено удачно. Найдено - {len(hh.data_from_vacancy)}")
sj.import_vacancy_from_api()  # импортируем данные с API SuperJobApi
sj.response_format()
print(f"Импорт с SJ завершено удачно. Найдено -{len(sj.data_from_vacancy)}")
jso = JsonSaver("Jso")  # Создаем объект класса JsonSaver
jso.import_from_api(hh, sj)  # создаем объекты класса Vacancy
print(f"Найдено всего {len(jso.vacancy_list)} вакансий")  # Проверяем создание объектов класса Vacancy
jso.add_vacancy()  # сохраняем в файл вакансии
print("Вакансии успешно сохранены в файл")
print(jso.check_file())

""" Импортируем данные с сохраненного файла"""
print()
print("Импортируем данные с сохраненного файла")
print(f"Количество вакансий до импорта {len(jso.vacancy_list)}")
jso.import_from_file()
print(f"Количество вакансий после импорта {len(jso.vacancy_list)}")

""" Выводим топ-5 вакансий по зарплате """
print()
print("ТОП-5 по зарплате")
for i in jso.top_salary():
    print(i)

"""ищем в созданных объектах Vacancy совпадения, если ничего не найдено вернет пустой список """
print()
res = []
z = True
while z:
    print("Введите слово для поиска среди найденных вакансий")
    text_search = input()
    res = jso.search_vacancy(text_search)
    if len(res) == 0:
        print("Совпадений не найдено")
    else:
        z = False
        for i in res:
            print(i)

"""Удаление результатов поиска из созданных объектов класса Vacancy """
print()
input("Нажмите Enter для удаления найденных результатов")
print(f"Количество вакансий до удаления {len(jso.vacancy_list)}")
for i in res:
    jso.del_vacancy(i.id_vacancy)
print(f"Количество вакансий после удаления {len(jso.vacancy_list)}")
