"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
	def __init__(self, title='Непонятно для чего это тут...'):
		self.title = title

	def draw(self):
		print('Запуск отрисовки')


class Pen(Stationery):
	def __init__(self, title='Непонятно для чего это тут...'):
		super().__init__(title)

	def draw(self):
		print('Запуск отрисовки - ручка')


class Pencil(Stationery):
	def __init__(self, title='Непонятно для чего это тут...'):
		super().__init__(title)

	def draw(self):
		print('Запуск отрисовки - карандаш')


class Handle(Stationery):
	def __init__(self, title='Непонятно для чего это тут...'):
		super().__init__(title)

	def draw(self):
		print('Запуск отрисовки - маркер')


Stationery().draw()
print(Stationery().title)
Pen().draw()
Pencil().draw()
Handle().draw()
print(Handle().title)
