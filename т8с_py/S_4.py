class Guitar:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self.__year = year

    def play(self):
        print(f"Играет {self._brand} {self._model}")

    def info(self):
        print(f"Гитара: {self._brand} {self._model}")

    def get_year(self):
        return self.__year

    def set_year(self, new_year):
        if 1950 <= new_year <= 2024:
            self.__year = new_year


guitar = Guitar("Fender", "Stratocaster", 1994)

guitar.info()
guitar.play()
print(f"Год выпуска: {guitar.get_year()}")

guitar.set_year(2020)
print(f"Новый год выпуска: {guitar.get_year()}")