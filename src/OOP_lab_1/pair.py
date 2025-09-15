class Pair:
    def __init__(self, first, second):
        if first >= second:
            raise ValueError("Ошибка: first должен быть меньше second.")
        self.first = first
        self.second = second

    def read(self):
        self.first = int(input("Введите начало интервала (first): "))
        self.second = int(input("Введите конец интервала (second): "))
        if self.first >= self.second:
            raise ValueError("Ошибка: first должен быть меньше second.")

    def display(self):
        print(f"[{self.first}, {self.second})")

    def rangecheck(self, number):
        return self.first <= number < self.second


def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    p1 = make_pair(3, 7)
    p1.display()
    print("Проверка числа 5 в интервале:", p1.rangecheck(5))
    print("Проверка числа 7 в интервале:", p1.rangecheck(7))

    p2 = Pair(0, 1)
    try:
        p2.read()
    except ValueError as e:
        print(e)
        exit(1)
    p2.display()
    num = int(input("Введите число для проверки: "))
    print("Число в интервале:", p2.rangecheck(num))
