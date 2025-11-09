class Tomato:
    states = ('отсутствует', 'цветение', 'зеленый', 'красный')

    def __init__(self, index: int):
        self._index = index
        self._state = Tomato.states[0]

    def grow(self) -> None:
        current_idx = Tomato.states.index(self._state)
        if current_idx < len(Tomato.states) - 1:
            self._state = Tomato.states[current_idx + 1]

    def is_ripe(self) -> bool:
        return self._state == Tomato.states[-1]

    def __repr__(self):
        return f"Tomato(index={self._index}, state='{self._state}')"


class TomatoBush:
    def __init__(self, tomato_count: int):
        self.tomatoes = [Tomato(i + 1) for i in range(tomato_count)]

    def grow_all(self) -> None:
        for t in self.tomatoes:
            t.grow()

    def all_are_ripe(self) -> bool:
        return all(t.is_ripe() for t in self.tomatoes)

    def give_away_all(self):
        harvest, self.tomatoes = self.tomatoes, []
        return harvest

    def __repr__(self):
        return f"TomatoBush(tomatoes={self.tomatoes})"


class Gardener:
    def __init__(self, name: str, plant: TomatoBush):
        self.name = name
        self._plant = plant

    def work(self) -> None:
        print(f"{self.name} ухаживает за кустом")
        self._plant.grow_all()
        print("Куст перешел на следующую стадию для всех плодов")

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Все плоды созрели. Сбор урожая")
            return self._plant.give_away_all()
        else:
            print("Внимание. Есть неспелые плоды. Рано собирать")
            return []

    @staticmethod
    def knowledge_base() -> None:
        print("Справка по садоводству")
        print("1. Полив и свет ускоряют рост растений")
        print("2. Слежение за стадиями развития помогает выбрать момент сбора")
        print("3. Урожай собирают только при полной спелости плодов")


if __name__ == "__main__":
    import io, sys

    console_capture = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = console_capture

    print("ТЕСТ 1 - СПРАВКА ПО САДОВОДСТВУ")
    Gardener.knowledge_base()

    print("\nТЕСТ 2 - СОЗДАНИЕ КУСТА И САДОВНИКА")
    bush = TomatoBush(tomato_count=3)
    print("Начальное состояние куста")
    print(bush)

    gardener = Gardener(name='Иван', plant=bush)
    print("Создан садовник", gardener.name)

    print("\nТЕСТ 3 - УХОД ЗА КУСТОМ")
    gardener.work()
    print("Текущее состояние", bush)

    print("\nТЕСТ 4 - ПОПЫТКА РАННЕГО СБОРА")
    picked = gardener.harvest()
    print("Собрано плодов", len(picked))

    print("\nПродолжаем уход до спелости")
    for i in range(3):
        if bush.all_are_ripe():
            break
        gardener.work()
        print("Состояние после ухода", bush)

    print("\nТЕСТ 5 - СБОР УРОЖАЯ")
    picked = gardener.harvest()
    print("Собрано плодов", len(picked))
    print("Куст после сбора", bush)

    sys.stdout = original_stdout
    print(console_capture.getvalue())
