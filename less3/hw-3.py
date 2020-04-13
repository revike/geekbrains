"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

print('\nЗадание 1\n')


def div(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        error = 'На ноль делить нельзя'
        return error


result = div(1, 100)
print(result)

'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''
print('\nЗадание 2\n')


def user_data(name, surname,
              year, city,
              email='did not indicate',
              tel='did not indicate'):
    result = surname.title() + ' ' \
             + name.title() + ' ' + year + \
             ' years old. From ' + city.title() \
             + '.\nE-mail: ' + email + '\nTel: ' + tel
    return result


user = user_data(name='Evgeny',
                 surname='Fedorin', year='1992', city='Nizhny Novgorod',
                 email='revike@ya.ru', tel='+7(929) 04 05 222')
print(user)

def user_data2(**kwargs):
    res = f"{kwargs['surname']} {kwargs['name']} {kwargs['year']} years old.\
 From {kwargs['city']}.\nE-mail: {kwargs['email']}\nTel: {kwargs['tel']}"
    return res

user = user_data2(name='Evgeny',
                 surname='Fedorin', year='1992', city='Nizhny Novgorod',
                 email='revike@ya.ru', tel='+7(929) 04 05 222')
print('\n' + user)

'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''
print('\nЗадание 3\n')


def my_func(a, b, c):
    list_a = [a, b, c]
    a1 = max(list_a)
    list_a.remove(a1)
    a2 = max(list_a)
    return a1, a2


print(my_func(10, 2, 3))

'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в
степень с помощью оператора **. Второй — более сложная реализация без
оператора **, предусматривающая использование цикла.
'''
print('\nЗадание 4\n')

x = 2
y = -5


def my_func1(x, y):
    res = x ** y
    return res


print(my_func1(x, y))


def my_func2(x, y):
    if y < 0:
        result = [x]
        i = -1
        while i > y:
            res = result[-1] * x
            result.append(res)
            i -= 1
        return 1 / result[-1]
    elif y == 0:
        return 1
    else:
        result = [x]
        i = 1
        while i < y:
            res = result[-1] * x
            result.append(res)
            i += 1
        return result[-1]


print(my_func2(x, y))

'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно 
добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''
print('\nЗадание 5\n')

user_num = input('Введите числа через пробел:')


def splits(user_num):
    """Разделяем числа"""
    res = user_num.split()
    return result(res)


def result(res):
    """Считаем результат"""
    amo = 0
    for result in res:
        if result != 'q':
            try:
                amo += int(result)
            except ValueError:
                pass
    return amo


def cont(user_num):
    """Добавление чисел или выход"""
    while True:
        add = input('\nq - Exit\nМожете добавить числа: ')
        if add == 'q':
            print(splits(user_num))
            break
        elif 'q' in add:
            user_num = user_num + ' ' + add
            print(splits(user_num))
            break
        else:
            user_num = str(user_num) + ' ' + add
            print(splits(user_num))


r1 = splits(user_num)
print(r1)
cont(r1)

'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text. 
Продолжить работу над заданием. В программу должна попадать строка
из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''
print('\nЗадание 6\n')


def int_func(text):
    return text.title()


print(int_func('test ok'))


int_func = lambda text: text.title()
print(int_func('test ok'))


def int_func2(text):
    """Меняет регистр всех символов латинских букв"""
    result = []
    for t in text:
        if chr(65) <= t <= chr(122):
            if t == t.lower():
                t = t.upper()
                result.append(t)
            else:
                t = t.lower()
                result.append(t)
        else:
            result.append(t)
    return ''.join(result)


print(int_func2('AqweRty sdfewFEFfsfd fewe . . ! fd 123rfe ПроГраМмер :)'))


def int_func3(text):
    """Меняет регистр только первой буквы слова"""
    result = []
    res = [text]
    for r in res:
        for i in r:
            result.append(i)
    result[0] = result[0].title()
    i = 0
    while i < len(result):
        if result[i] == ' ':
            try:
                result[i+1] = result[i+1].title()
            except IndexError:
                pass
        i += 1


    return ''.join(result)


print(int_func3('addwF dFs FsasF ! .. fFd '))
