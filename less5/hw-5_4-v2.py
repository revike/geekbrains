"""
4. Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from googletrans import Translator


def read_file(file):
    """Читаем исх файл"""
    with open(file, 'r', encoding='utf-8') as f:
        res = f.readlines()
        return trans(res)


def trans(res):
    """Перевод и запись"""
    new_file = 'task_4_result.txt'
    result = ''
    for i in res:
        res = Translator().translate(i, src='en', dest='ru')
        result += res.text + '\n'
        print(res.text)
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(result)


read_file('task_4.txt')

# 'task_4_result.txt' - результат в этом файле
