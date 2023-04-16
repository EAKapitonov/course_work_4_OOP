from class_from_api.superjob_api import SuperJobApi
from class_from_api.headhunter_api import HeadHunter
from vacancy.vacancy import Vacancy

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
hh.write_to_csv()  # записываем данные в файл csv
sj.write_to_csv()  # записываем данные в файл csv
hh.add_to_vacancy()  # создаем объекты класса Vacancy
print(len(Vacancy.vacancy_list))  # Проверяем создание объектов класса Vacancy, выдоим общее количество
sj.add_to_vacancy()  # создаем объекты класса Vacancy
print(len(Vacancy.vacancy_list))  # Проверяем создание объектов класса Vacancy, выдоим общее количество
hh.import_vacanсy_from_csv("./vacancy.csv")  # импортируем данные с файла csv и создаем объекты класса Vacancy
print(len(Vacancy.vacancy_list))  # Проверяем создание объектов класса Vacancy, выдоим общее количество
sj.import_vacanсy_from_csv("./superjob_vacancy.csv")  # импортируем данные с файла csv и создаем объекты класса Vacancy
print(len(Vacancy.vacancy_list))  # Проверяем создание объектов класса Vacancy, выдоим общее количество

"""
Выводим данные вакансии с наибольшей указанной зарплатой. 
"""
best_vacancy = Vacancy.vacancy_list[0]
for i in Vacancy.vacancy_list:
    if i > best_vacancy:
        best_vacancy = i
print(f"Лучшая указанная зарплата {best_vacancy.salary} "
      f"Ссылка на зарплату {best_vacancy.url}")

