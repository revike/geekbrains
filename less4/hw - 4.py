from functools import reduce
from itertools import count, cycle, islice
from math import factorial

"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
print('\nЗадание 2\n*****')

giv_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [k for k in giv_list[1:] if k > giv_list[giv_list.index(k) - 1]]
print(new_list)

"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
print('\nЗадание 3\n*****')

res = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(res)

"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
print('\nЗадание 4\n*****')

giv_l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

res = [k for k in giv_l if giv_l.count(k) < 2]
print(res)

"""
5. Реализовать формирование списка, используя функцию range() и
возможности генератора. В список должны войти четные числа от
100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
print('\nЗадание 5\n*****')

giv_list = [i for i in range(100, 1001) if i % 2 == 0]


def my_func(prev_el, el):
    return prev_el + el

print(f'result = {reduce(my_func, giv_list)}')

"""
6. Реализовать два небольших скрипта: 
а) итератор, генерирующий целые числа, начиная с указанного, 
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения. 
Например, в первом задании выводим целые числа, начиная с 3, а при
достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть
условие, при котором повторение элементов списка будет прекращено.

"""
print('\nЗадание 6 - (a)\n*****')

for res in count(3):
	if res > 10:
		break
	else:
		print(res)


print('\nЗадание 6 - (б)\n*****')

d_list = ['audi', 'bmw', 'suzuki', 'honda']

i = 0
for res in cycle(d_list):
	if i > 5:
		break
	else:
		print(res)
	i += 1


print('\nЗадание 6 - (*)\n*****')

# Так и не понял что дожно получиться тут) Единственное что я понял это использовать cycle() и count() без break;

r = input('Чет ввести надо: ')
try:
	k = int(input('И тут чет надо ввести: '))
except ValueError:
	k = (input('Или целое число, или я выключаюсь: '))
try:
	res = [f'{i} - {j}' for i in islice(count(int(k)), len(r))\
		   for j in islice(cycle(r.split()), int(k))]
	print(res)
except ValueError:
	print('Пока !)')


"""
7. Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо
выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

"""

print('\nЗадание 7\n*****')

def fact(arg):
	i = 1
	while i <= arg:
		res = factorial(i)
		yield f'Факториал {i}! = {res}'
		i += 1


for el in fact(5):
	print(el)
