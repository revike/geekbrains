"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Stock:
    """Склад оргтехники"""

    @staticmethod
    def reception():
        while True:
            name = (input('Что добавить на склад?\n1. Принтер\n2. Сканер\n3. Ксерокс'))
            if name == 'q':
                print('Склад!')
                Stock().read_stock()
                break
            try:
                if 0 < int(name) < 4:
                    print("===>")
                    brand = input('Введите бренд: ')
                    if brand == 'q':
                        print('Склад!')
                        Stock().read_stock()
                        break
                    model = input('Введите модель: ')
                    if model == 'q':
                        print('Склад!')
                        Stock().read_stock()
                        break

                    try:
                        price = input('Введите цену: ')
                        if price == 'q':
                            print('Склад!')
                            Stock().read_stock()
                            break
                        else:
                            price = int(price)
                    except ValueError:
                        print('\nError!\n')
                        continue
                    try:
                        quantity = input('Введите количество: ')
                        if quantity == 'q':
                            print('Склад!')
                            Stock().read_stock()
                            break
                        else:
                            quantity = int(quantity)
                    except ValueError:
                        print('\nError!\n')
                        continue

                    if name == '1':
                        color = input('Введите "1", если принтер черно-белый\nЕсли цветной, то просто нажмите Enter: ')
                        if color == '1':
                            Printer(brand, model, price, quantity, color=False).add_stock()
                        else:
                            Printer(brand, model, price, quantity).add_stock()
                    elif name == '2':
                        s_3d = input('Введите "1", если Сканер 3D\nЕсли обычный, то просто нажмите Enter: ')
                        if s_3d == '1':
                            Scanner(brand, model, price, quantity, s_3d=True).add_stock()
                        else:
                            Scanner(brand, model, price, quantity).add_stock()
                    elif name == '3':
                        analog = input('Введите "1", если Ксерокс аналоговый\nЕсли цифровой, то просто нажмите Enter: ')
                        if analog == '1':
                            Copier(brand, model, price, quantity, analog=True).add_stock()
                        else:
                            Copier(brand, model, price, quantity).add_stock()
                else:
                    print('\nНеверная команда\n')
                    continue
            except ValueError:
                print('\nНеверная команда\n')
                continue
            print('\t"q" - Exit')

    def read_stock(self):
        try:
            with open('stock.txt', encoding='utf-8') as f:
                result = f.read()
            print(result)
        except FileNotFoundError:
            pass


class OfficeEquipment:
    """Оргтехника"""

    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity

    def add_stock(self, name, optional):
        try:
            with open('stock.txt', encoding='utf-8') as f:
                res = f.read()
        except FileNotFoundError:
            with open('stock.txt', 'w', encoding='utf-8') as f:
                f.write('')

        if name == 1:
            res = f'Printer - {self.brand} $ Модель - {self.model} $ \
Цена - {int(self.price)} $ Количество - {int(self.quantity)} $ Цветной - {optional}'
        elif name == 2:
            res = f'Scanner - {self.brand} $ Модель - {self.model} $ \
Цена - {int(self.price)} $ Количество - {int(self.quantity)} $ 3D - {optional}'
        elif name == 3:
            res = f'Copier - {self.brand} $ Модель - {self.model} $ \
Цена - {int(self.price)} $ Количество - {int(self.quantity)} $ Аналоговый - {optional}'

        with open('stock.txt', 'a', encoding='utf-8') as f:
            f.write(res + '\n')


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, quantity, color=True):
        super().__init__(brand, model, price, quantity)
        self.color = color

    def add_stock(self):
        return OfficeEquipment(self.brand, self.model, self.price, self.quantity).add_stock(1, self.color)


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, quantity, s_3d=False):
        super().__init__(brand, model, price, quantity)
        self.s_3d = s_3d

    def add_stock(self):
        return OfficeEquipment(self.brand, self.model, self.price, self.quantity).add_stock(2, self.s_3d)


class Copier(OfficeEquipment):
    def __init__(self, brand, model, price, quantity, analog=False):
        super().__init__(brand, model, price, quantity)
        self.analog = analog

    def add_stock(self):
        return OfficeEquipment(self.brand, self.model, self.price, self.quantity).add_stock(3, self.analog)


Stock.reception()
