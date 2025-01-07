from autoclick import ClickHandler, ClickerWorker
from buttons import ButtonControl
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QThread
from PySide6.QtGui import QCloseEvent
from ui.window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('MTZ Auto-Clicker')
        self.statusBar.showMessage('Beta - v0.5')
        self.setFixedSize(self.width(), self.height())

        self.buttons = ButtonControl(self, self.leftModeButton, self.rightModeButton)

        self.leftModeButton.clicked.connect(self.buttons.m_LeftModeClicked)
        self.rightModeButton.clicked.connect(self.buttons.m_RightModeClicked)
        self.bindMouseButton.clicked.connect(self.buttons.m_BindButton)

        self.click_listener = ClickHandler(cpsInterval=1/self.cpsMouseSpin.value())
        self.click_listener.start_capture()

        self.leftModeButton.clicked.connect(lambda: self.click_listener.set_side('left'))
        self.rightModeButton.clicked.connect(lambda: self.click_listener.set_side('right'))

        self.buttons.bindWindow.keybindSignal.connect(lambda key: self.click_listener.change_keybind(key))
        self.cpsMouseSpin.valueChanged.connect(lambda value: self.click_listener.set_cpsInterval(value))

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

