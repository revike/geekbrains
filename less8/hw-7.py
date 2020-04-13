"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


#  Вариант 1
class ComplexNumber:
	def __init__(self, arg):
		self.arg = arg

	def __add__(self, other):
		return f'Сложение - {self.arg + other.arg}'

	def __mul__(self, other):
		return f'Умножение - {self.arg * other.arg}'


compl_1 = complex(2, -6)
compl_2 = complex(5, 2)

print(compl_1 + compl_2)
print(compl_1 * compl_2)
print('=' * 10)
a = ComplexNumber(compl_1)
b = ComplexNumber(compl_2)

print(a + b)
print(a * b)


#  Вариант 2
class ComplexNumber2:
	def __init__(self, arg):
		self.arg = arg

	def __add__(self, other):
		return f'Сложение = {self.arg[0] + other.arg[0]} + ({self.arg[1] + other.arg[1]})*i'

	def __mul__(self, other):
		return f'Умножение = {self.arg[0] * other.arg[0] - self.arg[1] * other.arg[1]} + ({self.arg[1] * other.arg[0] + self.arg[0] * other.arg[1]})*i'


print('\n\nКомплексное число - a + b*i')
while True:
	try:
		a1 = int(input('Введите "а" первого комплексного числа: '))
		b1 = int(input('Введите "b" первого комплексного числа: '))
		a2 = int(input('Введите "а" второго комплексного числа: '))
		b2 = int(input('Введите "b" второго комплексного числа: '))
		k1 = [a1, b1]
		k2 = [a2, b2]
		com1 = ComplexNumber2(k1)
		com2 = ComplexNumber2(k2)

		print(com1 + com2)
		print(com1 * com2)
		break
	except ValueError:
		print('\nНужно вводить только числа!\nПопробуем сначала\n')
		continue
