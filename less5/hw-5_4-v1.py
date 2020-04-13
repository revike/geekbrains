"""
4. Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


def read_file(file):
    """Читаем исх файл"""
    with open(file, 'r', encoding='utf-8') as f:
        res = f.readlines()
        return trans(res)


def trans(res):
    """Перевод"""
    result = []
    for i in res:
        if i.split('-')[1].strip() == '1':
            result.append('Один - 1\n')
        if i.split('-')[1].strip() == '2':
            result.append('Два - 2\n')
        if i.split('-')[1].strip() == '3':
            result.append('Три - 3\n')
        if i.split('-')[1].strip() == '4':
            result.append('Четыре - 4\n')
    return write_new_file(result)


def write_new_file(result):
    """Записываем перевод в новый файл"""
    new_file = 'task_4_res.txt'
    with open(new_file, 'w', encoding='utf-8') as f:
        for wr in result:
            f.write(wr)

read_file('task_4.txt')


# 'task_4_res.txt' - Результат в этом файле
