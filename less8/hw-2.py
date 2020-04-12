"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Except(Exception):
    def __init__(self, arg):
        self.arg = arg

    @staticmethod
    def calc():
        while True:
            try:
                a = input('Введите делимое: ')
                if a == 'q':
                    break
                b = input('Введите делитель: ')
                if b == 'q':
                    break
                try:
                    if int(b) == 0:
                        raise Except('\nНа ноль делить нельзя!\n')
                except Except as ex:
                    print(ex)
                else:
                    res = float(a) / float(b)
                    print(f'Результат - {res:.2f}')
                    print('\n"q" - Exit!\n')
            except ValueError:
                print('Введите числа!\n')


Except.calc()
