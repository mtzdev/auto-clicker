from PySide6.QtWidgets import QMainWindow
from ui.window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('MTZ Auto-Clicker')
        self.statusBar.showMessage('Beta - v0.01')
        self.setFixedSize(self.width(), self.height())