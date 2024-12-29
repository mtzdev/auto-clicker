from PySide6.QtWidgets import QPushButton
from display import KeyBindWindow
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main_window import MainWindow

# m_ = mouse group box
# k_ = keyboard group box

class ButtonControl:
    def __init__(self, main_window: 'MainWindow', LMouseModeButton: QPushButton, RMouseModeButton: QPushButton):
        self.window = main_window
        self.leftMouseModeButton = LMouseModeButton
        self.rightMouseModeButton = RMouseModeButton
        self.MouseActiveMode = 'left'
        self.bindWindow = KeyBindWindow()
        self.bindWindow.keybindSignal.connect(lambda keybind: self.window.BindMLineEdit.setText(keybind))

    def m_LeftModeClicked(self):
        self.leftMouseModeButton.setDisabled(True)
        self.rightMouseModeButton.setDisabled(False)
        self.window.modeMLabel.setFocus()
        self.MouseActiveMode = 'left'

    def m_RightModeClicked(self):
        self.leftMouseModeButton.setDisabled(False)
        self.rightMouseModeButton.setDisabled(True)
        self.window.modeMLabel.setFocus()
        self.MouseActiveMode = 'right'

    def m_BindButton(self):
        self.bindWindow.show()


