"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random


def new_file(file, a, b):
    """Создаем файл"""
    k = random.randrange(a)
    i = 0
    with open(file, 'w', encoding='utf-8') as f:
        while i < k:
            wr_file = f.write(str(random.randrange(b)) + ' ')
            i += 1
    read_file(file)


def read_file(file):
    """Читаем файл"""
    with open(file, 'r', encoding='utf-8') as f:
        r_file = f.read()
        return result(r_file)

def result(r_file):
    result = 0
    for res in r_file.split():
        result += int(res)
    print(f'Сумма чисел в файле = {result}')


new_file('task_5.txt', 100, 500)
