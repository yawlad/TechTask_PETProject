import peewee
from models import *
from db import *
import os
import sys


class App():

    def __init__(self) -> None:
        self.database = DATABASE_OBJ
        self.database.connect()
        self.database.create_tables([Vacancy, Skill])
        self.keys = {
            "1": self.input_vacancy,
            "2": self.destroy_vacancy_by_name,
            "3": self.get_all_vacancies,
            "4": self.get_vacancy,
            "5": self.exit,
        }

    def start_app(self, message='Выберите пункт:'):
        os.system('CLS')
        print(f"\n{message} \n")
        print("1. Добавить запись в бд")
        print("2. Удалить запись из бд по названию")
        print("3. Просмотреть все записи из бд")
        print("4. Найти запись в бд по названию вакансии")
        print("5. Выход\n")
        try:
            self.keys[input("Ваш выбор: ")]()
        except KeyError:
            self.start_app(message='Выберете существующий пункт:')

    def input_vacancy(self):
        os.system('CLS')
        print("\nВведите данные: \n")
        try:
            name = input("1. Название: ")
            description = input("2. Описание: ")
            salary = int(input("3. Зарплата (в долларах): "))
            type = input("4. Тип работы (удаленная / смешанная /в офисе): ")
            if type not in ('удаленная', 'смешанная', 'в офисе'):
                raise Exception
            skills = input("5. Требуемые навыки (через пробел): ").split(' ')
        except:
            self.start_app(message="Некорректный ввод")
        vac = Vacancy.create(
            name=name, description=description, salary=salary, work_type=type)
        for skill in skills:
            Skill.create(name=skill, owner=vac)
        self.start_app(message='Успешно добавлено')

    def destroy_vacancy_by_name(self):
        os.system('CLS')
        try:
            vacancy = Vacancy.get(Vacancy.name == input(
                "Введите название вакансии: ")).delete_instance()
            self.start_app(message='Успешно удалено')
        except:
            self.start_app(message='Имя не найдено')

    def get_all_vacancies(self):
        os.system('CLS')
        vacancies = Vacancy.select()
        for vacancy in vacancies:
            print(f'==='*20)
            print(f'Имя: {vacancy.name}')
            print(f'Описание: {vacancy.description}')
            print(f'Зарплата: {vacancy.salary}')
            print(f'Тип: {vacancy.work_type}')
            print(f'Навыки: ')
            for skill in Skill.select().where(Skill.owner == vacancy):
                print(f'\t * {skill.name}')
        print(f'==='*20)
        print(f'Всего {Vacancy.select().count()} вакансий')
        print(f'==='*20)
        input('Нажмите enter, чтобы вернуться в меню')
        self.start_app()

    def get_vacancy(self):
        os.system('CLS')
        vacancies = Vacancy.select().where(
            Vacancy.name.contains(input("Введите название вакансии: ")))
        for vacancy in vacancies:
            print(f'==='*20)
            print(f'Имя: {vacancy.name}')
            print(f'Описание: {vacancy.description}')
            print(f'Зарплата: {vacancy.salary}')
            print(f'Тип: {vacancy.work_type}')
            print(f'Навыки: ')
            for skill in Skill.select().where(Skill.owner == vacancy):
                print(f'\t * {skill.name}')
        print(f'==='*20)
        print(f'По вашему запросу нашлось {vacancies.count()} вакансий')
        print(f'==='*20)
        input('Нажмите enter, чтобы вернуться в меню')
        self.start_app()

    def exit(self):
        sys.exit(0)


App().start_app()