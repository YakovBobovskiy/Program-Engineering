class Car:  # Объявление класса Car
    def __init__(self, make, model):  # Конструктор класса
        self.make = make  # Сохраняем марку автомобиля
        self.model = model  # Сохраняем модель автомобиля

    def drive(self):  # Метод drive
        print(f"Driving the {self.make} {self.model}")  # Выводим информацию

# Создание объекта класса Car
my_car = Car("Toyota", "Corolla")  # Передаем марку и модель в конструктор
my_car.drive() # Вызов метода drive для объекта my_car