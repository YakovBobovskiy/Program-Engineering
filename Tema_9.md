\# Тема 9. ООП на Python: концепции, принципы и примеры реализации

Отчет по Теме #9 выполнил(а):

\- Бобовский Яков Евгеньевич

\- ИВТ-23-1



| Задание | Лаб\_раб | Сам\_раб |

| ------ | ------ | ------ |

| Задание 1 | + | + |

| Задание 2 | + |  |

| Задание 3 | + |  |

| Задание 4 | + |  |

| Задание 5 | + |  |



знак "+" - задание выполнено; знак "-" - задание не выполнено;



Работу проверили:

\- к.э.н., доцент Панов М.А.	



\## Лабораторная работа №1

\### Создайте класс, который будет проверять угадал ли человек ваше имя или нет. Сделайте проверку в функции init(). Проверьте что будет, если вызвать атрибут, который не указан в классе.



\*\*Код:\*\*



```python

class Ivan:

&nbsp;   \_\_slots\_\_ = \['name']



&nbsp;   def \_\_init\_\_(self, name):

&nbsp;       if name == 'Иван':

&nbsp;           self.name = f"Да, я {name}"

&nbsp;       else:

&nbsp;           self.name = f"Я не {name}, а Иван"



person1 = Ivan('Алексей')

person2 = Ivan('Иван')

print(person1.name)

print(person2.name)



person2.surname = 'Петров'

```



\*\*Результат:\*\*



!\[т9л\_1](т9л\_pic/т9л\_1.png)



\*\*Выводы:\*\* Использован \_\_slots\_\_ для ограничения атрибутов класса. При попытке добавить несуществующий атрибут возникает ошибка AttributeError.



\## Лабораторная работа №2

\### Написать программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения.



\*\*Код:\*\*



```python

class Icecream:

&nbsp;   def \_\_init\_\_(self, ingridient=None):

&nbsp;       if isinstance(ingridient, str):

&nbsp;           self.ingridient = ingridient

&nbsp;       else:

&nbsp;           self.ingridient = None



&nbsp;   def composition(self):

&nbsp;       if self.ingridient:

&nbsp;           print(f"Мороженое с {self.ingridient}")

&nbsp;       else:

&nbsp;           print('Обычное мороженое')



icecream = Icecream()

icecream.composition()

icecream = Icecream('шоколадом')

icecream.composition()

icecream = Icecream(5)

icecream.composition()

```



\*\*Результат:\*\*



!\[т9л\_2](т9л\_pic/т9л\_2.png)



\*\*Выводы:\*\* Реализована проверка типа входных данных в конструкторе. Класс корректно обрабатывает строки и другие типы данных для топпинга.



\## Лабораторная работа №3

\### Реализуйте класс с инкапсуляцией, включающий сеттер, геттер и деструктор. Продемонстрируйте работу всех функций.



\*\*Код:\*\*



```python

class MyСlass:

&nbsp;   def \_\_init\_\_(self, value):

&nbsp;       self.\_value = value



&nbsp;   def set\_value(self, value):

&nbsp;       self.\_value = value



&nbsp;   def get\_value(self):

&nbsp;       return self.\_value



&nbsp;   def del\_value(self):

&nbsp;       del self.\_value



&nbsp;   value = property(get\_value, set\_value, del\_value, "Свойство value")



obj = MyСlass(42)

print(obj.get\_value())

obj.set\_value(45)

print(obj.get\_value())

obj.set\_value(100)

print(obj.get\_value())

obj.del\_value()

print(obj.get\_value())

```



\*\*Результат:\*\*



!\[т9л\_3](т9л\_pic/т9л\_3.png)



\*\*Выводы:\*\* Создан класс с полной инкапсуляцией, включающий геттер, сеттер и деструктор для управления атрибутом value.



\## Лабораторная работа №4

\### Написать три класса: Кошки, Собаки, Млекопитающие. И при помощи “наследования” объяснить компьютеру что кошки и собаки – это млекопитающие. Добавьте уникальные атрибуты для кошек и собак.



\*\*Код:\*\*



```python

class Mammal:

&nbsp;   className = 'Mammal'



class Dog(Mammal):

&nbsp;   species = 'canine'

&nbsp;   sounds = 'wow'



class Cat(Mammal):

&nbsp;   species = 'feline'

&nbsp;   sounds = 'meow'



dog = Dog()

print(f"Dog is {dog.className}, but they say: {dog.sounds}")

cat = Cat()

print(f"Cat is {cat.className}, but they say: {cat.sounds}")

```



\*\*Результат:\*\*



!\[т9л\_4](т9л\_pic/т9л\_4.png)



\*\*Выводы:\*\* Построена иерархия наследования: классы Dog и Cat наследуются от Mammal, демонстрируя отношение "является".



\## Лабораторная работа №5

\### Реализуйте полиморфизм с классами для разных языков приветствия. Используйте декоратор @staticmethod.



\*\*Код:\*\*



```python

class Russian:

&nbsp;   @staticmethod

&nbsp;   def greeting():

&nbsp;       print("Привет")



class English:

&nbsp;   @staticmethod

&nbsp;   def greeting():

&nbsp;       print("Hello")



def greet(language):

&nbsp;   language.greeting()



ivan = Russian()

greet(ivan)

john = English()

greet(john)

```



\*\*Результат:\*\*



!\[т9л\_5](т9л\_pic/т9л\_5.png)



\*\*Выводы:\*\* Реализован полиморфизм через статические методы с декоратором @staticmethod для разных языков приветствия.



\## Самостоятельная работа №1  

\### Садовник и помидоры. Реализовать систему классов: Tomato, TomatoBush, Gardener с полным жизненным циклом выращивания томатов.



\*\*Код:\*\*



```python

class Tomato:

&nbsp;   states = ('отсутствует', 'цветение', 'зеленый', 'красный')



&nbsp;   def \_\_init\_\_(self, index: int):

&nbsp;       self.\_index = index

&nbsp;       self.\_state = Tomato.states\[0]



&nbsp;   def grow(self) -> None:

&nbsp;       current\_idx = Tomato.states.index(self.\_state)

&nbsp;       if current\_idx < len(Tomato.states) - 1:

&nbsp;           self.\_state = Tomato.states\[current\_idx + 1]



&nbsp;   def is\_ripe(self) -> bool:

&nbsp;       return self.\_state == Tomato.states\[-1]



&nbsp;   def \_\_repr\_\_(self):

&nbsp;       return f"Tomato(index={self.\_index}, state='{self.\_state}')"





class TomatoBush:

&nbsp;   def \_\_init\_\_(self, tomato\_count: int):

&nbsp;       self.tomatoes = \[Tomato(i + 1) for i in range(tomato\_count)]



&nbsp;   def grow\_all(self) -> None:

&nbsp;       for t in self.tomatoes:

&nbsp;           t.grow()



&nbsp;   def all\_are\_ripe(self) -> bool:

&nbsp;       return all(t.is\_ripe() for t in self.tomatoes)



&nbsp;   def give\_away\_all(self):

&nbsp;       harvest, self.tomatoes = self.tomatoes, \[]

&nbsp;       return harvest



&nbsp;   def \_\_repr\_\_(self):

&nbsp;       return f"TomatoBush(tomatoes={self.tomatoes})"





class Gardener:

&nbsp;   def \_\_init\_\_(self, name: str, plant: TomatoBush):

&nbsp;       self.name = name

&nbsp;       self.\_plant = plant



&nbsp;   def work(self) -> None:

&nbsp;       print(f"{self.name} ухаживает за кустом")

&nbsp;       self.\_plant.grow\_all()

&nbsp;       print("Куст перешел на следующую стадию для всех плодов")



&nbsp;   def harvest(self):

&nbsp;       if self.\_plant.all\_are\_ripe():

&nbsp;           print("Все плоды созрели. Сбор урожая")

&nbsp;           return self.\_plant.give\_away\_all()

&nbsp;       else:

&nbsp;           print("Внимание. Есть неспелые плоды. Рано собирать")

&nbsp;           return \[]



&nbsp;   @staticmethod

&nbsp;   def knowledge\_base() -> None:

&nbsp;       print("Справка по садоводству")

&nbsp;       print("1. Полив и свет ускоряют рост растений")

&nbsp;       print("2. Слежение за стадиями развития помогает выбрать момент сбора")

&nbsp;       print("3. Урожай собирают только при полной спелости плодов")





if \_\_name\_\_ == "\_\_main\_\_":

&nbsp;   import io, sys



&nbsp;   console\_capture = io.StringIO()

&nbsp;   original\_stdout = sys.stdout

&nbsp;   sys.stdout = console\_capture



&nbsp;   print("ТЕСТ 1 - СПРАВКА ПО САДОВОДСТВУ")

&nbsp;   Gardener.knowledge\_base()



&nbsp;   print("\\nТЕСТ 2 - СОЗДАНИЕ КУСТА И САДОВНИКА")

&nbsp;   bush = TomatoBush(tomato\_count=3)

&nbsp;   print("Начальное состояние куста")

&nbsp;   print(bush)



&nbsp;   gardener = Gardener(name='Иван', plant=bush)

&nbsp;   print("Создан садовник", gardener.name)



&nbsp;   print("\\nТЕСТ 3 - УХОД ЗА КУСТОМ")

&nbsp;   gardener.work()

&nbsp;   print("Текущее состояние", bush)



&nbsp;   print("\\nТЕСТ 4 - ПОПЫТКА РАННЕГО СБОРА")

&nbsp;   picked = gardener.harvest()

&nbsp;   print("Собрано плодов", len(picked))



&nbsp;   print("\\nПродолжаем уход до спелости")

&nbsp;   for i in range(3):

&nbsp;       if bush.all\_are\_ripe():

&nbsp;           break

&nbsp;       gardener.work()

&nbsp;       print("Состояние после ухода", bush)



&nbsp;   print("\\nТЕСТ 5 - СБОР УРОЖАЯ")

&nbsp;   picked = gardener.harvest()

&nbsp;   print("Собрано плодов", len(picked))

&nbsp;   print("Куст после сбора", bush)



&nbsp;   sys.stdout = original\_stdout

&nbsp;   print(console\_capture.getvalue())

```



\*\*Результат:\*\*



!\[т9с\_1](т9с\_pic/т9с\_1.png)



\*\*Выводы:\*\* Создана сложная система классов (Tomato, TomatoBush, Gardener) с полным жизненным циклом выращивания томатов и статическим методом для справки.



\## Общие выводы по теме

В ходе выполнения лабораторных и самостоятельных работ по теме №9 были углублены знания объектно-ориентированного программирования в Python. Рассмотрены продвинутые концепции ООП: механизм \_\_slots\_\_ для оптимизации памяти, свойства (property) для управления доступом к атрибутам, статические методы и декораторы. Освоено построение сложных иерархий классов с реализацией полного жизненного цикла объектов. Особое внимание уделено практическому применению инкапсуляции через геттеры и сеттеры, созданию статических методов для утилитарных функций и проектированию взаимосвязанных классов. Выполненные задания способствовали формированию навыков разработки сложных объектно-ориентированных систем, что является основой для создания масштабируемых приложений на Python.

