COLOR = "Green"  # глобальные переменные
VOICE = "RRRRR"


class Animal:  # создаём класс
    def __init__(self, color: str, voice: str):  # метод, который используется для инициализации (добавления параметров)
        self.color = color
        self.voice = voice

    def make_voice(self) -> str:  # функция, которая тоже может что-то делать с параметрами
        return self.voice


tiger = Animal(COLOR, VOICE)  # создаем объект созданного класса, в скобках пишем параметры, нужные для __init__
print(tiger.make_voice())  # можем вызывать какие-то функции из класса


class Cat(Animal):  # создаем подкласс - имеет те же вещи + можем добавить что-то отдельное
    def attack(self):  # новая функция
        return self.voice + "\nI don't like it."  # мы можем использовать то, что есть только в Animal


lion = Cat(COLOR, VOICE)  # объект, который теперь дополнительно имеет новую функцию
print(lion.attack())  # вызываем новую функцию
print(lion.make_voice())  # но старые, несмотря на то, что мы их не написали заново, тоже будут работать
