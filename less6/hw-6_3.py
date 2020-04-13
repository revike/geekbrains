"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.surname.title()} {self.name.title()}.\nДолжность - {self.position}')

    def get_total_income(self):
        try:
            print(f"Зарплата - {int(self._income['wage']) + int(self._income['bonus'])}")
        except ValueError:
            print('Оклад и премию необходимо вводить числами!')


def input_data():
    """получаем данные и выводим результат"""
    name = input('Введите имя сотрудника: ')
    surname = input('Введите фамилия сотрудника: ')
    position = input('Введите должность: ')
    wage = input('Введите оклад: ')
    bonus = input('Введите примию: ')
    income = {"wage": wage, "bonus": bonus}
    print('=>\nЗначения экземпляров:')
    res = Position(name, surname, position, income)
    res.get_full_name()
    res.get_total_income()
    print('\nЗначения атрибутов:')
    print(res.name)
    print(res.surname)
    print(res.position)
    print(res._income)


input_data()
