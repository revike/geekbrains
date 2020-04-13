"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def input_data(file):
    """Записываем в файл"""
    data = input('Введите данный, которые нужно записать в файл: ')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(data + '\n')
    while True:
        data = input('Введите данный, которые нужно записать в файл: ')
        if data == '':
            break
        else:
            with open(file, 'a', encoding='utf-8') as f:
                f.write(data + '\n')
    return read_data(file)


def read_data(file):
    """Считаем строки, слова и символы"""
    with open(file, 'r', encoding='utf-8') as f:
        res = f.readlines()

    score_str = len(res)
    print(f'\nВ Файле {file} количество строк - {score_str}\n')  # кол-во строк

    for i, result in enumerate(res, 1):
        print(f'В {i}ой строке слов - {len(result.split())}')  # кол-во слов

    print('\n')

    for k, res_in in enumerate(res, 1):
        print(f"В {k}ой строке букв - {len(''.join(res_in.rstrip().split()))}")  # кол-во букв


input_data('task_1-2.txt') # результат в этом файле
