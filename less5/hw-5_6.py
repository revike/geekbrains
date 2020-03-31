"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по
этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def read_file(file):
    """Читаем файл"""
    file = 'task_6.txt'
    with open(file, 'r', encoding='utf-8') as f:
        result = (f.read())
    return num_of_clas(result)


def num_of_clas(result):
    """Считаем кол-во занятий"""
    list_less = result.split('\n')
    list_num = []
    for i in list_less:
        k = i.split(':')[1].split()
        p = i.split(':')[0]
        total = 0
        for j in k:
            res = j.split('(')[0]
            try:
                total += int(res)
            except ValueError:
                continue
        list_num.append(p + ' ' + str(total))
    return dict_input(list_num)


def dict_input(list_num):
    """Выводим словарь на экран"""
    result = {}
    for i in list_num:
        result[i.split()[0]] = int(i.split()[1])
    print(result)


read_file('task_6.txt')
