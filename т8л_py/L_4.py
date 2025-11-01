class Car:  # Объявление класса Car
    def __init__(self, make, model):  # Конструктор класса
        self._make = make  # Защищенный атрибут марки
        self.__model = model  # Приватный атрибут модели

    def drive(self):  # Метод drive
        print(f"Driving the {self._make} {self.__model}")  # Выводим информацию

# Создание объекта класса Car
my_car = Car("Toyota", "Corolla")  # Передаем марку и модель в конструктор
print(my_car._make)  # Доступ к защищенному атрибуту
my_car.drive() # Вызов метода drive для объекта my_car