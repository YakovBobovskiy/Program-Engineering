class Guitar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def play(self):
        print(f"Играет {self.brand} {self.model}")

    def info(self):
        print(f"Гитара: {self.brand} {self.model}")

guitar = Guitar("Fender", "Stratocaster")

guitar.info()
guitar.play()