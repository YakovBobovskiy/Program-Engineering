# Базовый класс для всех фигур
class Shape:
    def area(self):
        pass  # Метод будет переопределен в дочерних классах

# Класс прямоугольника, наследуется от Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width   # Ширина прямоугольника
        self.height = height # Высота прямоугольника

    # Переопределяем метод area для прямоугольника
    def area(self):
        return self.width * self.height  # Площадь = ширина * высота

# Класс круга, наследуется от Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Радиус круга

    # Переопределяем метод area для круга
    def area(self):
        return 3.14 * self.radius * self.radius  # Площадь = π * r² (используем 3.14 как π)

# Создаем массив фигур
shapes = [
    Rectangle(5, 10),  # Прямоугольник 5x10
    Circle(7)          # Круг с радиусом 7
]

# Выводим площади всех фигур
for shape in shapes:
    print(f"Площадь фигуры: {shape.area()}")  # Полиморфизм: один метод для разных типов фигур