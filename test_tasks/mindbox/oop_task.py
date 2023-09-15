'''Задание:
Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и
треугольника по трем сторонам. Дополнительно к работоспособности оценим:
- Юнит-тесты
- Легкость добавления других фигур
- Вычисление площади фигуры без знания типа фигуры в compile-time
- Проверку на то, является ли треугольник прямоугольным'''
import math
from abc import ABC, abstractmethod


# создаём абстрактный класс всех фигур
class Figure(ABC):

    def __init__(self):
        self._perimeter, self._area = None, None

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()
        list_of_lengths = sorted([a, b, c], reverse=True)
        if any(i <= 0 for i in list_of_lengths):
            raise ValueError('неположительные числа для длины недопустимы')
        if list_of_lengths[0] >= list_of_lengths[1] + list_of_lengths[2]:
            raise ValueError('Сумма двух длин сторон треугольника равна или меньше длины третьей стороны')
        self._lengths = list_of_lengths
        self._is_right = None

    @property
    def is_right(self):  # можно через if-elif-else, но так проще
        if self._is_right is None:
            if self._lengths[0] ** 2 == self._lengths[1] ** 2 + self._lengths[2] ** 2:
                self._is_right = True
            else:
                self._is_right = False
        return self._is_right

    @property
    def perimeter(self):
        if not self._perimeter:
            self._perimeter = sum(self._lengths)
        return self._perimeter

    @property
    def area(self):
        if self.is_right:
            return self._lengths[1] * self._lengths[2] / 2
        p = self.perimeter / 2
        return pow(p * (p - self._lengths[0]) * (p - self._lengths[1]) * (p - self._lengths[2]), 0.5)


class Circle(Figure):
    def __init__(self, r):
        super().__init__()
        if r <= 0:
            raise ValueError('неположительные числа для радиуса недопустимы')
        self._r = r

    @property
    def perimeter(self):
        if not self._perimeter:
            self._perimeter = 2 * math.pi * self._r
        return self._perimeter

    @property
    def area(self):
        if not self._area:
            self._area = math.pi * self._r ** 2
        return self._area


if __name__ == "__main__":

    triangle_2 = Triangle(4, 3, 5)
    triangle_3 = Triangle(1, 2, 2)

    circle_1 = Circle(3)
    circle_2 = Circle(1 / math.pi)

    #print(triangle_1.perimeter, triangle_1.area)
    print(triangle_2.perimeter, triangle_2.area)
    print(triangle_3.perimeter, triangle_3.area)
    print(circle_1.perimeter, circle_1.area)
    print(circle_2.perimeter, circle_2.area)
    print(triangle_2.is_right, triangle_3.is_right)

    #triangle_1 = Triangle(1, 2, 3)
    #triangle_1 = Triangle(1, -2, 3)
    #circle_3 = Circle(-1)