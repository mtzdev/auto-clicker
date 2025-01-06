from pynput.keyboard import Listener, KeyCode
from PySide6.QtCore import QObject, Signal

class ClickListener(QObject):
    keyPressed = Signal()

    def __init__(self, keybind = ''):
        super().__init__()
        self.keybind = keybind
        self.listener = Listener(on_release=self.on_release)

    def start_capture(self):
        self.listener.start()

    def stop_capture(self):
        self.listener.stop()

    def change_keybind(self, key):
        self.keybind = key.lower()

    def on_release(self, key):
        if key == KeyCode.from_char(self.keybind):
            self.keyPressed.emit()
