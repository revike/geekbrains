"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json


def read_file(file):
    """Читаем файл"""
    with open(file, 'r', encoding='utf-8') as f:
        res = f.read().split('\n')
        return profit(res)


def profit(res):
    """Считаем прибыль"""
    result = [] # список компаний
    result_prof = [] # прибыльные компании
    result_les = [] # убыточные компании
    for prof in res:
        profit = int(prof.split()[2]) - int(prof.split()[3])
        if profit:
            result.append(prof.split()[0] + ' ' + str(profit))
        if profit > 0:
            result_prof.append(prof.split()[0] + ' ' + str(profit))
        else:
            result_les.append(prof.split()[0] + ' ' + str(profit))
    result_ave = average_profit(result_prof) # словарь со средней прибылью
    return list_dict(result, result_ave)


def average_profit(result_prof):
    """Средняя прибыль"""
    res = 0
    for ave_prof in result_prof:
        res += int(ave_prof.split()[1])
    result = res / len(result_prof)
    return {"average_profit": int(result)}


def list_dict(result, result_ave):
    """Создаем итоговый список"""
    total = []
    total_dict = {}
    for i in result:
        total_dict[i.split()[0]] = int(i.split()[1])
    total.append(total_dict)
    total.append(result_ave)
    return write_json(total)


def write_json(total):
    """Записываем в json"""
    with open('tesk_7_res.json', 'w', encoding='utf-8') as f:
        json.dump(total, f, ensure_ascii=False,
                  sort_keys=False, indent=4, separators=(',', ': '))


read_file('task_7.txt')

# task_7_res.json - результат
