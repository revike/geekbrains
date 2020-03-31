"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        res = f.read()
        return sal_low(res)


def sal_low(res):
    result = res.split('\n')
    for i in result:
        if float(i.split()[1]) < 20000:
            print(f'{i.split()[0]} - имеет зп меньше 20000')
    sal_ave(result)


def sal_ave(result):
    total = 0
    for s in result:
        total += float(s.split()[1])
    res = total / len(result)
    print(f'\nСредняя зп = {res:.2f}')

read_file('task_3.txt')
