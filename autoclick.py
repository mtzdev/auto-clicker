from time import sleep
from pynput import mouse
from pynput.keyboard import Listener, KeyCode
from PySide6.QtCore import QObject, Signal, Slot

class ClickHandler(QObject):
    keyPressed = Signal()

    def __init__(self, keybind = '', cpsInterval = 0.1):
        super().__init__()
        self.keybind = keybind
        self.isRunning = False
        self.cpsInterval = cpsInterval
        self.side = mouse.Button.left
        self.listener = Listener(on_release=self.on_release)

    @Slot()
    def toggle(self):
        self.isRunning = not self.isRunning

    def set_cpsInterval(self, value):
        self.cpsInterval = 1/value

    def set_side(self, side):
        if side == 'left':
            self.side = mouse.Button.left
        elif side == 'right':
            self.side = mouse.Button.right
        else:
            print('Error: Invalid side')

    def start_capture(self):
        self.listener.start()

    def change_keybind(self, key):
        self.keybind = key.lower()

    def on_release(self, key):
        if key == KeyCode.from_char(self.keybind):
            self.keyPressed.emit()


class ClickerWorker(QObject):
    clickFinished = Signal()

    def __init__(self, click):
        super().__init__()
        self.is_app_active = True
        self.clickHandler = click
        self.mouse_controller = mouse.Controller()

    @Slot()
    def run(self):
        while self.is_app_active:
            if self.clickHandler.isRunning:
                self.mouse_controller.click(self.clickHandler.side, 1)
                sleep(self.clickHandler.cpsInterval)
            else:
                sleep(0.2)