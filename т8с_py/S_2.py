class Guitar:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def play(self):
        print(f"Играет {self.brand} {self.model}")

    def info(self):
        print(f"Гитара: {self.brand} {self.model}")

guitar = Guitar("Fender", "Stratocaster", 1994)

guitar.info()
guitar.play()
print(f"Год выпуска: {guitar.year}")