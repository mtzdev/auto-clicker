from autoclick import ClickHandler, ClickerWorker
from buttons import ButtonControl
from db import get_config, CpsConfigSave, update_mouse_bind, update_mouse_side
from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import QThread
from PySide6.QtGui import QCloseEvent
from ui.window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('MTZ Auto-Clicker')
        self.setFixedSize(self.width(), self.height())

        # DB
        config = get_config()
        self.cpsMouseSpin.setValue(config['mouse']['cps'])
        self.BindMLineEdit.setText(config['mouse']['bind'].upper())

        # Status Bar
        github_label = QLabel('Developed by mtz - <a href="https://github.com/mtzdev/auto-clicker/" style="color: #2D8CEC;">GitHub Repo</a>')
        github_label.setOpenExternalLinks(True)  # Permitir abrir o link
        self.statusBar.addWidget(github_label)

        # Botões / Conexões
        self.buttons = ButtonControl(self, self.leftModeButton, self.rightModeButton)
        mouse_side = {
            'left': self.buttons.m_LeftModeClicked,
            'right': self.buttons.m_RightModeClicked
        }
        mouse_side.get(config['mouse']['side'], self.buttons.m_RightModeClicked)()
        self.buttons.bindWindow.keybind = config['mouse']['bind'].upper()

        self.leftModeButton.clicked.connect(self.buttons.m_LeftModeClicked)
        self.rightModeButton.clicked.connect(self.buttons.m_RightModeClicked)
        self.bindMouseButton.clicked.connect(self.buttons.m_BindButton)

        self.click_listener = ClickHandler(keybind=config['mouse']['bind'])
        self.click_listener.set_cpsInterval(config['mouse']['cps'])
        self.click_listener.set_side(config['mouse']['side'])
        self.click_listener.start_capture()

        self.leftModeButton.clicked.connect(lambda: self.click_listener.set_side('left'))
        self.rightModeButton.clicked.connect(lambda: self.click_listener.set_side('right'))

        self.buttons.bindWindow.keybindSignal.connect(lambda key: self.click_listener.change_keybind(key))
        self.cpsMouseSpin.valueChanged.connect(lambda value: self.click_listener.set_cpsInterval(value))

        # DB connects
        mouse = CpsConfigSave('mouse')
        self.cpsMouseSpin.valueChanged.connect(lambda value: mouse.update_cps(value))
        self.buttons.bindWindow.keybindSignal.connect(lambda key: update_mouse_bind(key))
        self.leftModeButton.clicked.connect(lambda: update_mouse_side('left'))
        self.rightModeButton.clicked.connect(lambda: update_mouse_side('right'))

        self.createClicker()

    def createClicker(self):
        self.clickThread = QThread()
        self.clicker = ClickerWorker(self.click_listener)
        self.clicker.moveToThread(self.clickThread)

        self.clickThread.started.connect(self.clicker.run)
        self.click_listener.keyPressed.connect(self.click_listener.toggle)

        self.clickThread.start()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.clicker.is_app_active = False
        self.clickThread.quit()
        self.clickThread.wait()
        return super().closeEvent(event)

