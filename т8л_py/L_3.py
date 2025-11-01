class Car:  # Объявление класса Car
    def __init__(self, make, model):  # Конструктор класса
        self.make = make  # Сохраняем марку автомобиля
        self.model = model  # Сохраняем модель автомобиля

    def drive(self):  # Метод drive
        print(f"Driving the {self.make} {self.model}")  # Выводим информацию

# Создание объекта класса Car
my_car = Car("Toyota", "Corolla")  # Передаем марку и модель в конструктор
my_car.drive() # Вызов метода drive для объекта my_car


class ElectricCar(Car):  # Класс (наследник Car)
    def __init__(self, make, model, battery_capacity):  # Конструктор
        super().__init__(make, model)  # Вызов конструктора родителя
        self.battery_capacity = battery_capacity  # Емкость батареи

    def charge(self):  # Метод зарядки
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")  # Сообщение о зарядке

# Создаем объект ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 75)  # Новая Tesla Model S
my_electric_car.drive() # Вызываем унаследованный метод
my_electric_car.charge() # Вызываем собственный метод