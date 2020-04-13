"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

from datetime import datetime as dt


class Date:
	def __init__(self, date):
		self.date = date

	@classmethod
	def int_date(cls, date):
		try:
			res = [int(i) for i in date.split('-')]
			for i in res:
				print(f'{i} - {type(i)}')
		except ValueError:
			pass

	@staticmethod
	def valid(date):
		try:
			list_date = [int(i) for i in date.split('-')]

			day = list_date[0]
			month = list_date[1]
			year = list_date[2]

		
			if month == 2:
				if (year % 4 == 0 or year % 400 == 0) and (year % 100 != 0): # Високосный год должен быть кратным 4, но при этом не должен быть кратным 100, или год кратен 400.
					if (0 < day <= 29):
						pass
				elif (year % 4 != 0 or year % 100 == 0) and year % 400 != 0: # Год не является високосным (высокосным), если он не кратен 4, либо он кратен 100, но в этом случае не кратен 400
					if (0 < day < 29):
						pass
					else:
						print('Неверно введен день')
			elif 1 <= month <= 7:
				if (month % 2 != 0) and (0 < day < 31):
					pass
				elif (month % 2 == 0) and (0 < day < 30):
					pass
				else:
					print('Неверно введен день')
			elif 8 <= month <= 12:
				if (month % 2 == 0) and (0 < day < 31):
					pass
				elif (month % 2 != 0) and (0 < day < 30):
					pass
				else:
					print('Неверно введен день')
			else:
				print('Неверно введен месяц')
		except ValueError:
			print('Неверная дата')


	def run_int_date(self):
		return Date.int_date(self.date)

	def run_valid(self):
		return Date.valid(self.date)



print('*' * 15)
date_now = dt.now().date().strftime('%d-%m-%Y')
int_date = Date(date_now).run_int_date()
valid_date = Date(date_now).run_valid()
print('*' * 15)
date1 = '31-06-1954'
int_date = Date(date1).run_int_date()
valid_date = Date(date1).run_valid()
print('*' * 15)
date2 = '41-01-2016'
int_date = Date(date2).run_int_date()
valid_date = Date(date2).run_valid()
print('*' * 15)
date3 = '29-02-2019'
int_date = Date(date3).run_int_date()
valid_date = Date(date3).run_valid()
print('*' * 15)
date4 = '29-24-2019'
int_date = Date(date4).run_int_date()
valid_date = Date(date4).run_valid()
print('*' * 15)
date5 = '29-02-2020'
int_date = Date(date5).run_int_date()
valid_date = Date(date5).run_valid()
print('*' * 15)
date6 = '29-02-500'
int_date = Date(date6).run_int_date()
valid_date = Date(date6).run_valid()
