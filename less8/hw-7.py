"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


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
