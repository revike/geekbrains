"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
	def __init__(self, speed, color, name):
		self.speed = speed
		self.color = color
		self.name = name

	def go(self):
		print(f'Car {self.name.title()} color {self.color} go!')

	def stop(self):
		print(f'Car {self.name.title()} color {self.color} stop!')

	def turn(self, direction):
		print(f'Car {self.name.title()} color {self.color} turn {direction}')

	def show_speed(self):
		print(f'Speed = {self.speed}')


class TownCar(Car):
	def __init__(self, speed, color, name):
		super().__init__(speed, color, name)

	def show_speed(self):
		if self.speed > 60:
			print('Превышение скорости!')


class SportCar(Car):
	def __init__(self, speed, color, name):
		super().__init__(speed, color, name)


class WorkCar(Car):
	def __init__(self, speed, color, name):
		super().__init__(speed, color, name)

	def show_speed(self):
		if self.speed > 40:
			print('Превышение скорости!')


class PoliceCar(Car):
	def __init__(self, speed, color, name, is_police):
		self.is_police = is_police
		super().__init__(speed, color,name)

	def police(self):
		if self.is_police:
			print(f'{self.name.title()} is Police Car')


TownCar(70, 'write', 'audi').go()
TownCar(70, 'write', 'audi').turn('left')
TownCar(70, 'red', 'audi').show_speed()
TownCar(70, 'red', 'audi').stop()
print('*' * 5)
SportCar(210, 'red', 'ferrari').go()
SportCar(210, 'red', 'ferrari').show_speed()
print('*' * 5)
PoliceCar(20, 'black', 'vaz;)', True).go()
PoliceCar(20, 'green', 'uaz', True).police()
