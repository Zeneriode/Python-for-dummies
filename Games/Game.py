class Car:
    def __init__(self, color):
        self.avg_speed = 100
        self.audio = "rrrrr"
        self.color = color

    def increase_speed(self) -> None:
        print("Скорость автомобиля сейчас:", end=" ")
        for speed in range(0, self.avg_speed, 10):
            print(str(speed) + "...", end=" ")
        print()

    def say_color(self) -> str:
        return "Цвет машины: " + self.color


# lamborghini = Car("Yellow")
# lamborghini.increase_speed()
# print(lamborghini.say_color())
# print(lamborghini.color)

class Lamborghini(Car):
    def __init__(self, color, display):
        super().__init__(color)
        self.display = display
        self.avg_speed = 300

    def increase_speed(self) -> None:
        print("Скорость автомобиля сейчас:", end=" ")
        for speed in range(0, self.avg_speed, 50):
            print(str(speed) + "...", end=" ")
        print("Автомобиль приехал в пункт назначения.")


lambo = Lamborghini("Green", "Ipad 5")
lambo.increase_speed()
print(lambo.say_color())
