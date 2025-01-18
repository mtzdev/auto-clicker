from time import sleep
from pynput import mouse
from pynput.keyboard import Listener, KeyCode, Controller, Key
from PySide6.QtCore import QObject, Signal, Slot

SPECIAL_KEYS = {
    'Shift': Key.shift,
    'Control': Key.ctrl,
    'Alt': Key.alt,
    'Esc': Key.esc,
    'Meta': Key.cmd,
    'Backspace': Key.backspace,
    'Enter': Key.enter,
    'Return': Key.enter,
    'Space': Key.space,
    'Tab': Key.tab,
    'Left': Key.left,
    'Right': Key.right,
    'Up': Key.up,
    'Down': Key.down,
    'CapsLock': Key.caps_lock,
    'F1': Key.f1,
    'F2': Key.f2,
    'F3': Key.f3,
    'F4': Key.f4,
    'F5': Key.f5,
    'F6': Key.f6,
    'F7': Key.f7,
    'F8': Key.f8,
    'F9': Key.f9,
    'F10': Key.f10,
    'F11': Key.f11,
    'F12': Key.f12,
    'Ins': Key.insert,
    'Delete': Key.delete,
    'Home': Key.home,
    'End': Key.end,
    'PgUp': Key.page_up,
    'PgDown': Key.page_down,
    'Pause': Key.pause,
    'PrintScreen': Key.print_screen,
    'NumLock': Key.num_lock,
    'ScrollLock': Key.scroll_lock,
    'Menu': Key.menu,
    'Clear': None
}

class m_ClickHandler(QObject):
    keyPressed = Signal()

    def __init__(self, keybind = ''):
        super().__init__()
        self.keybind = keybind
        self.isRunning = False
        self.cpsInterval = 0.1
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

class k_ClickHandler(QObject):
    keyPressed = Signal()

    def __init__(self, keybind = ''):
        super().__init__()
        self.keybind = keybind
        self.isRunning = False
        self.cpsInterval = 0.1
        self.keyClicker = None
        self.listener = Listener(on_release=self.on_release)

    @Slot()
    def toggle(self):
        if not self.keyClicker:
            return
        self.isRunning = not self.isRunning

    def set_cpsInterval(self, value):
        self.cpsInterval = 1/value

    def set_keyClicker(self, key):
        if key in SPECIAL_KEYS:
            self.keyClicker = SPECIAL_KEYS[key]
        else:
            self.keyClicker = key

    def start_capture(self):
        self.listener.start()

    def change_keybind(self, key):
        self.keybind = key.lower()

    def on_release(self, key):
        if key == KeyCode.from_char(self.keybind):
            self.keyPressed.emit()


class m_ClickerWorker(QObject):
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

class k_ClickerWorker(QObject):
    def __init__(self, click):
        super().__init__()
        self.is_app_active = True
        self.clickHandler = click
        self.keyboard_controller = Controller()

    @Slot()
    def run(self):
        while self.is_app_active:
            if self.clickHandler.isRunning:
                self.keyboard_controller.tap(self.clickHandler.keyClicker)
                sleep(self.clickHandler.cpsInterval)
            else:
                sleep(0.2)
