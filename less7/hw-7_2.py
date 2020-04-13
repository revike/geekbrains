"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
	@abstractmethod
	def v(self):
		pass

	@abstractmethod
	def h(self):
		pass


class Coat(Clothes):
	def __init__(self, v):
		self.v = v

	def h(self):
		pass

	@property
	def v(self):
		return self._v

	@v.setter
	def v(self, v):
		if v < 1:
			self._v = 1
		elif v > 5:
			self._v = 5
		else:
			self._v = v

	def cloth(self):
		res = self.v / 6.5 + 0.5
		return f'На пальто необходимо {res:.1f} м ткани.'



class Costume(Clothes):
	def __init__(self, h):
		self.h = h

	def v(self):
		pass

	@property
	def h(self):
		return self._h

	@h.setter
	def h(self, h):
		if h < 1:
			self._h = 1
		elif h > 5:
			self._h = 5
		else:
			self._h = h

	def cloth(self):
		res = 2 * self.h + 0.3
		return f'На костюм необходимо {res:.1f} м ткани.'
		
		

coat = Coat(5)
print(coat.cloth())

costume = Costume(-5)
print(costume.cloth())
