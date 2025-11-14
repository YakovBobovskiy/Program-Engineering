# Класс исключения
class NegativeNumberError(Exception):
    def __init__(self, value, message="Отрицательные числа не допускаются"):
        self.value = value                    # Сохраняем ошибочное значение
        self.message = f"{message}: {value}"  # Формируем сообщение об ошибке
        super().__init__(self.message)        # Передаем сообщение в родительский класс

# Функция вычисления квадратного корня
def calculate_square_root(number):
    if number < 0:    # Проверяем число на отрицательность
        raise NegativeNumberError(number, "Нельзя вычислить корень из отрицательного числа")  # Выбрасываем исключение
    return number ** 0.5  # Возвращаем результат вычисления

# Функция создания банковского счета
def create_user_account(age, balance):
    if age < 0:       # Проверяем возраст на отрицательность
        raise NegativeNumberError(age, "Возраст не может быть отрицательным")  # Выбрасываем исключение
    if balance < 0:   # Проверяем баланс на отрицательность
        raise NegativeNumberError(balance, "Баланс не может быть отрицательным")  # Выбрасываем исключение
    return f"Счет создан! Возраст: {age}, Баланс: {balance}"  # Возвращаем успешный результат

# Тестирование работы исключений
print("Тест 1: Квадратный корень")
try:
    print(f"Корень 25 = {calculate_square_root(25)}")  # Успешный вызов функции
    calculate_square_root(-4)                     # Вызов с отрицательным числом
except NegativeNumberError as e:
    print(f"Ошибка: {e}")                         # Обработка исключения

print("\nТест 2: Создание счета")
try:
    print(create_user_account(25, 1000))          # Успешный вызов функции
    create_user_account(-5, 500)                  # Вызов с отрицательным возрастом
except NegativeNumberError as e:
    print(f"Ошибка: {e}")                         # Обработка исключения

print("\nТест 3: Отрицательный баланс")
try:
    create_user_account(30, -100)                 # Вызов с отрицательным балансом
except NegativeNumberError as e:
    print(f"Ошибка: {e}")                         # Обработка исключения