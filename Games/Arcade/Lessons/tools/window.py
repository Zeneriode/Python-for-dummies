"""
Объяснение класса Window.
Чтобы начать делать какую-либо игру, нужно сначала создать окно, в которой всё будет происходить.
Для этого тут используется класс Window, который создаёт пустое окно, способное меняться под требования игры.

Для создания собственного окна нужно создать класс, который будет наследовать свойства класса Window
"""

from arcade import run, Window


class MyWindow(Window):
    """Простое окно размеров 800х600"""

    def __init__(self):
        super().__init__()  # Передаём все параметры для создания окна

        # Параметры окна, которые можно изменить
        # Все эти параметры желательно инициализировать при запуске конструктора класса Window (стр. 16)
        self.width = 800  # Ширина окна
        self.height = 600  # Высота экрана
        self.title = "Test"  # Название окна
        self.set_fullscreen(False)  # Делать окно полноэкранным или нет
        self.resizeable = False  # Разрешить менять размеры окна или нет
        self.update_rate = 1 / 60  # 1 / fps или как часто обновлять кадр
        self.visible = True  # показывать окно сразу при запуске или нет
        self.vsync = False  # стараться синхронизировать изображения или нет
        self.center_window = True  # Показать окно в центре экрана
        self.enable_polling = True  # Можно ли использовать мышь / клавиатуру / другое для окна

    def setup(self):
        """Метод, где обычно загружаются и создаются все предметы для конкретного уровня или режима"""
        pass

    def on_draw(self):
        """Рисует все объекты на экране"""
        pass

    def on_hide(self):
        """Активируется, если пользователь уменьшил окно или свернул его"""
        pass

    def on_show(self):
        """Активируется, если пользователь заново открыл окно после сворачивания"""
        pass

    def on_expose(self):
        """Активируется, если пользователь переключился на другое окно"""
        pass

    def on_activate(self):
        """Активируется, когда выбирается окно, то есть когда оно самое главное сейчас"""
        pass

    def on_text(self, text):
        """Активируется последним в случае, когда пользователь ввел какой-то текст"""
        pass

    def on_file_drop(self, x, y, paths):
        """Если в окно пытались добавить какие-либо файлы"""
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        """Активируется, если пользователь нажал на какую-либо кнопку"""
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        """Активируется, если пользователь отжал какую-либо кнопку"""
        pass

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        """Метод для добавления функционала для мыши"""
        pass

    def on_mouse_enter(self, x: int, y: int):
        """Вызывается, если мышь была сдвинута"""
        pass

    def on_mouse_leave(self, x: int, y: int):
        """Вызывается, если мышь вышла за пределы окна"""
        pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        """Вызывается, если пользователь подвинул мышь"""
        pass

    def on_update(self, delta_time: float):
        """Метод для обновления всех предметов. Вызывается каждый кадр"""
        pass


if __name__ == "__main__":
    window = MyWindow()
    # window.setup()
    run()
