class Car: # Объявление класса Car
    def __init__(self, make, model): # Конструктор класса
        self.make = make    # Сохраняем марку автомобиля
        self.model = model  # Сохраняем модель автомобиля

# Создание объекта класса Car
my_car = Car("Toyota", "Corolla")  # Передаем марку и модель в конструктор