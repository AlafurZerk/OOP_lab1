
class River:
# список всех рек
all_rivers = []
def _init__(self, name, length) :
self.name = name
self.length = length
# добавляем текущую реку в список всех рек
River.all_rivers.append(self)
volga = River("волга"
, 3530)
seine = River("Сена"
, 776)
nile = River("нил", 6852)
# далее печатаем все названия рек
for river in River.all_rivers:
print(river.name)

class River:
    # список всех рек
    all_rivers = []

    def init(self, name, length):
        self.name = name
        self.length = length
        # добавляем текущую реку в список всех рек
        River.all_rivers.append(self)

volga = River("Волга", 3530)
seine = River("Сена", 776)
nile = River("Нил", 6852)

# далее печатаем все названия рек
for river in River.all_rivers:
    print(river.name)
# output:
# Волга
# Сена
# Нил

# Класс River с методом get_info
class River:
    all_rivers = []

    def init(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)

    def get_info(self):
        print("Длина {0} равна {1} км".format(self.name, self.length))

volga = River("Волга", 3530)
seine = River("Сена", 776)
nile = River("Нил", 6852)

volga.get_info()
# Длина Волги равна 3530 км
seine.get_info()
# Длина Сены равна 776 km
nile.get_info()
# Длина Нила равна 6852 km

# Класс Pet с атрибутами класса и экземпляра
class Pet:
    kind = "mammal"
    n_pets = 0  # количество питомцев
    pet_names = []  # список имен всех питомцев

    def init(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4

# Создание экземпляров
tom = Pet("cat", "Tom")
avocado = Pet("dog", "Avocado")
ben = Pet("goldfish", "Benjamin")

# Работа с атрибутом класса n_pets
# Изменение через класс
Pet.n_pets += 3

print(Pet.n_pets)    # 3
print(tom.n_pets)    # 3
print(avocado.n_pets)   # 3
print(ben.n_pets)    # 3

# Изменение через экземпляры (создает атрибуты экземпляра)
tom.n_pets += 1
avocado.n_pets += 1
ben.n_pets += 1

print(Pet.n_pets)    # 3
print(tom.n_pets)    # 4
print(avocado.n_pets)    # 4
print(ben.n_pets)    # 4

# Работа с атрибутом класса kind
ben.kind = "fish"

print(Pet.kind)    # "mammal"
print(tom.kind)    # "mammal"
print(avocado.kind)    # "mammal"
print(ben.kind)    # "fish"

# Работа с изменяемым атрибутом класса pet_names
Pet.pet_names.append(tom.name)
Pet.pet_names.append(avocado.name)
Pet.pet_names.append(ben.name)

print(Pet.pet_names)  # ["Tom", "Avocado", "Benjamin"]
print(tom.pet_names)  # ["Tom", "Avocado", "Benjamin"]
print(avocado.pet_names)  # ["Tom", "Avocado", "Benjamin"]
print(ben.pet_names)  # ["Tom", "Avocado", "Benjamin"]

# Создание отдельных списков для каждого экземпляра
tom.pet_names = ["Tom"]
avocado.pet_names = ["Avocado"]
ben.pet_names = ["Benjamin"]

print(Pet.pet_names)  # ["Tom", "Avocado", "Benjamin"]
print(tom.pet_names)  # ["Tom"]
print(avocado.pet_names)  # ["Avocado"]
print(ben.pet_names)  # ["Benjamin"]

# Класс Ship с методом и отдельная функция
class Ship:
    def init(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0


    def sail(self):
        print("{} has sailed!".format(self.name))


def sail_function(name):
    print("{} has sailed!".format(name))

# Создание экземпляра и вызов метода
black_pearl = Ship("Black Pearl", 100)
black_pearl.sail()  # prints "Black Pearl has sailed!"

# Вызов функции
sail_function("Black Pearl")  # prints "Black Pearl has sailed!"


# Класс Rectangle с защищенными атрибутами
class Rectangle:
    def init(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, w):
        self._width = w

    def get_height(self):
        return self._height

    def set_height(self, h):
        self._height = h

    def area(self):
        return self._width * self._height


# Пример использования
rect = Rectangle(10, 20)
print(rect.get_width())  # 10
print(rect._width)  # 10 (можно обратиться напрямую)

class Rectangle:
    def init(self, width, height):
        self.width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, w):
        self.__width = w

    def get_height(self):
        return self.__height

    def set_height(self, h):
        self.__height = h

    def area(self):
        return self.__width * self.__height


# Пример использования
rect = Rectangle(10, 20)
print(rect.get_width())  # 10

# Попытка обратиться напрямую вызовет ошибку
# rect.__width  # AttributeError: 'Rectangle' object has no attribute '__width'

# Но можно обратиться через измененное имя
print(rect._Rectangle__width)  # 10
rect._Rectangle__width = 20
print(rect.get_width())  # 20


#  Класс Ship с методами load_cargo и unload_cargo
class Ship:
    def __init(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def load_cargo(self, weight):
        if self.cargo + weight <= self.capacity:
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight):
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons".format(weight))
        else:
            print("Cannot unload that much")


# Пример использования
black_pearl = Ship("Black Pearl", 1000)
black_pearl.load_cargo(600)  # "Loaded 600 tons"
black_pearl.unload_cargo(400)  # "Unloaded 400 tons"
black_pearl.load_cargo(700)  # "Cannot load that much"
black_pearl.unload_cargo(300)  # "Cannot unload that much"

class Rational:
    def init(self, a=0, b=1):
        a = int(a)
        b = int(b)

        if b == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = abs(a)
        self.__denominator = abs(b)
        self.__reduce()

    # Сокращение дроби
    def __reduce(self):
        # Функция для нахождения наибольшего общего делителя
        def gcd(a, b):
            if a == 0:
                return b
            elif b == 0:
                return a
            elif a >= b:
                return gcd(a % b, b)
            else:
                return gcd(a, b % a)

        c = gcd(self.__numerator, self.__denominator)
        self.__numerator //= c
        self.__denominator //= c

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    # Прочитать значение дроби с клавиатуры
    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split('/', maxsplit=1)))

        if parts[1] == 0:
            raise ValueError("Denominator cannot be zero")

        self.__numerator = abs(parts[0])
        self.__denominator = abs(parts[1])
        self.__reduce()

    # Вывести дробь на экран
    def display(self):
        print(f"{self.numerator}/{self.denominator}")

    # Сложение обыкновенных дробей
    def add(self, rhs):
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator + \
                self.denominator * rhs.numerator
            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError("Argument must be Rational")

    # Вычитание обыкновенных дробей
    def sub(self, rhs):
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator - \
                self.denominator * rhs.numerator
            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError("Argument must be Rational")

    # Умножение обыкновенных дробей
    def mul(self, rhs):
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.numerator
            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError("Argument must be Rational")

    # Деление обыкновенных дробей
    def div(self, rhs):
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator
            b = self.denominator * rhs.numerator
            return Rational(a, b)
        else:
            raise ValueError("Argument must be Rational")

    # Проверка на равенство дробей
    def equals(self, rhs):
        if isinstance(rhs, Rational):
            return (self.numerator == rhs.numerator) and \
                (self.denominator == rhs.denominator)
        else:
            return False

    # Проверка на больше
    def greater(self, rhs):
        if isinstance(rhs, Rational):
            v1 = self.numerator / self.denominator
            v2 = rhs.numerator / rhs.denominator
            return v1 > v2
        else:
            return False

    # Проверка на меньше
    def less(self, rhs):
        if isinstance(rhs, Rational):
            v1 = self.numerator / self.denominator
            v2 = rhs.numerator / rhs.denominator
            return v1 < v2
        else:
            return False


if __name == 'main':
    r1 = Rational(3, 4)
    r1.display()  # 3/4

    r2 = Rational()
    r2.read("Введите обыкновенную дробь: ")
    r2.display()

    r3 = r2.add(r1)
    r3.display()

    r4 = r2.sub(r1)
    r4.display()

    r5 = r2.mul(r1)
    r5.display()

    r6 = r2.div(r1)
    r6.display()