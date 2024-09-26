class Figure:
    def __init__(self, color, *sides):
        self.__sides = list()
        self.__color = list(color)
        self.filled = True

        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == len(self.__sides) and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * 3.141592653589793) if self.get_sides() else 0

    def get_square(self):
        return 3.141592653589793 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Площадь по формуле Герона
        return area


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 0:
            sides = [1]  # если стороны не переданы, используем 1
        super().__init__(color, *([sides[0]] * self.sides_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Пример проверки
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # Должно вывести: [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # Должно вывести: [222, 35, 130]

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # Должно вывести: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # Должно вывести: [15]

# Проверка периметра (круга), это и есть длина
print(len(circle1))  # Должно вывести: 15

# Проверка объёма (куба)
print(cube1.get_volume())  # Должно вывести: 216

# Проверка площади круга
print(circle1.get_square())  # Площадь круга

# Проверка площади треугольника
triangle1 = Triangle((100, 150, 200), 3, 4, 5)  # Пример: треугольник со сторонами 3, 4, 5
print(triangle1.get_square())  # Должно вывести: 6.0