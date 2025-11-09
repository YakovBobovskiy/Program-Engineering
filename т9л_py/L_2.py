class Icecream:
    def __init__(self, ingridient=None):
        if isinstance(ingridient, str):
            self.ingridient = ingridient
        else:
            self.ingridient = None

    def composition(self):
        if self.ingridient:
            print(f"Мороженое с {self.ingridient}")
        else:
            print('Обычное мороженое')

icecream = Icecream()
icecream.composition()
icecream = Icecream('шоколадом')
icecream.composition()
icecream = Icecream(5)
icecream.composition()