from autoclick import m_ClickHandler, m_ClickerWorker, k_ClickHandler, k_ClickerWorker
from buttons import ButtonControl
import db
from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import QThread, Slot
from PySide6.QtGui import QCloseEvent
from typing import Literal
from ui.window import Ui_MainWindow

# prefix:
# m_ = mouse
# k_ = keyboard

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('MTZ Auto-Clicker')
        self.setFixedSize(self.width(), self.height())

        # DB
        config = db.get_config()
        self.cpsMouseSpin.setValue(config['mouse']['cps'])
        self.BindMLineEdit.setText(config['mouse']['bind'].upper())
        self.cpsKBSpin.setValue(config['keyboard']['cps'])
        self.bindKBLineEdit.setText(config['keyboard']['bind'].upper())
        self.clickBindKB.setText(config['keyboard']['keyDisplay'].upper())

        # Status Bar
        github_label = QLabel('Developed by mtz - <a href="https://github.com/mtzdev/auto-clicker/" style="color: #2D8CEC;">GitHub Repo</a>')
        github_label.setOpenExternalLinks(True)  # Permitir abrir o link
        self.statusBar.addWidget(github_label)

        # Buttons
        self.buttons = ButtonControl(self, self.leftModeButton, self.rightModeButton)

        mouse_side = {
            'left': self.buttons.m_LeftModeClicked,
            'right': self.buttons.m_RightModeClicked
        }
        mouse_side.get(config['mouse']['side'], self.buttons.m_RightModeClicked)()

        self.leftModeButton.clicked.connect(self.buttons.m_LeftModeClicked)
        self.rightModeButton.clicked.connect(self.buttons.m_RightModeClicked)
        self.bindMouseButton.clicked.connect(self.buttons.m_BindButton)

        self.buttons.m_bindWindow.keybindReset.connect(lambda: self.resetBind('mouse'))
        self.buttons.k_bindWindow.keybindReset.connect(lambda: self.resetBind('keyboardBind'))
        self.buttons.k_clickWindow.keybindReset.connect(lambda: self.resetBind('keyboardClick'))

        # Mouse
        self.mouse_handler = m_ClickHandler(keybind=config['mouse']['bind'])
        self.mouse_handler.set_cpsInterval(config['mouse']['cps'])
        self.mouse_handler.set_side(config['mouse']['side'])
        self.mouse_handler.start_capture()

        self.leftModeButton.clicked.connect(lambda: self.mouse_handler.set_side('left'))
        self.rightModeButton.clicked.connect(lambda: self.mouse_handler.set_side('right'))
        self.cpsMouseSpin.valueChanged.connect(lambda value: self.mouse_handler.set_cpsInterval(value))
        self.buttons.m_bindWindow.keybindSignal.connect(lambda key: self.mouse_handler.change_keybind(key))

        self.createMouseClicker()

        # Keyboard
        self.keyboard_handler = k_ClickHandler(keybind=config['keyboard']['bind'])
        self.keyboard_handler.set_cpsInterval(config['keyboard']['cps'])
        self.keyboard_handler.set_keyClicker(config['keyboard']['key'])
        self.keyboard_handler.start_capture()

        self.bindKBButton.clicked.connect(self.buttons.k_BindButton)
        self.clickBindButton.clicked.connect(self.buttons.k_ClickerButton)

        self.cpsKBSpin.valueChanged.connect(lambda value: self.keyboard_handler.set_cpsInterval(value))
        self.buttons.k_bindWindow.keybindSignal.connect(lambda keybind: self.keyboard_handler.change_keybind(keybind))
        self.buttons.k_clickWindow.keybindSignal.connect(lambda _, key_code: self.keyboard_handler.set_keyClicker(key_code))

        self.createKeyboardClicker()

        # DB Save
        db_cps_mouse = db.CpsConfigSave('mouse')
        db_cps_keyboard = db.CpsConfigSave('keyboard')
        self.cpsMouseSpin.valueChanged.connect(lambda value: db_cps_mouse.update_cps(value))
        self.cpsKBSpin.valueChanged.connect(lambda value: db_cps_keyboard.update_cps(value))

        self.buttons.m_bindWindow.keybindSignal.connect(lambda key: db.update_mouse_bind(key))
        self.buttons.k_bindWindow.keybindSignal.connect(lambda keybind: db.update_keyboard_bind(keybind))
        self.buttons.k_clickWindow.keybindSignal.connect(lambda keybind, key_code: (db.update_keyboard_keydisplay(keybind), db.update_keyboard_key(key_code)))

        self.leftModeButton.clicked.connect(lambda: db.update_mouse_side('left'))
        self.rightModeButton.clicked.connect(lambda: db.update_mouse_side('right'))

    def createMouseClicker(self):
        self.clickMouseThread = QThread()
        self.clickerMouse = m_ClickerWorker(self.mouse_handler)
        self.clickerMouse.moveToThread(self.clickMouseThread)

        self.clickMouseThread.started.connect(self.clickerMouse.run)
        self.mouse_handler.keyPressed.connect(self.mouse_handler.toggle)

        self.clickMouseThread.start()

    def createKeyboardClicker(self):
        self.clickKeyboardThread = QThread()
        self.clickerKeyboard = k_ClickerWorker(self.keyboard_handler)
        self.clickerKeyboard.moveToThread(self.clickKeyboardThread)

        self.clickKeyboardThread.started.connect(self.clickerKeyboard.run)
        self.keyboard_handler.keyPressed.connect(self.keyboard_handler.toggle)

        self.clickKeyboardThread.start()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.clickerMouse.is_app_active = False
        self.clickerKeyboard.is_app_active = False

        self.clickMouseThread.quit()
        self.clickKeyboardThread.quit()

        self.clickMouseThread.wait()
        self.clickKeyboardThread.wait()
        return super().closeEvent(event)

    @Slot()
    def resetBind(self, mode: Literal['mouse', 'keyboardBind', 'keyboardClick']):
        if mode == 'mouse':
            self.BindMLineEdit.clear()
            self.mouse_handler.change_keybind('')
            db.update_mouse_bind('')
        if mode == 'keyboardBind':
            self.bindKBLineEdit.clear()
            self.keyboard_handler.change_keybind('')
            db.update_keyboard_bind('')
        if mode == 'keyboardClick':
            self.clickBindKB.clear()
            self.keyboard_handler.set_keyClicker('')
            db.update_keyboard_key('')
            db.update_keyboard_keydisplay('')
