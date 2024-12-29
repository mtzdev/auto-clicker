from PySide6.QtWidgets import QMainWindow
from ui.window import Ui_MainWindow
from buttons import ButtonControl

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('MTZ Auto-Clicker')
        self.statusBar.showMessage('Beta - v0.01')
        self.setFixedSize(self.width(), self.height())

        self.buttons = ButtonControl(self, self.leftModeButton, self.rightModeButton)

        self.leftModeButton.clicked.connect(self.buttons.m_LeftModeClicked)
        self.rightModeButton.clicked.connect(self.buttons.m_RightModeClicked)
        self.bindMouseButton.clicked.connect(self.buttons.m_BindButton)