from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton
from display import KeyBindWindow, KeyClickerWindow
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
        self.m_bindWindow = KeyBindWindow('mouse')
        self.k_bindWindow = KeyBindWindow('keyboard')
        self.k_clickWindow = KeyClickerWindow()
        self.m_bindWindow.keybindSignal.connect(lambda keybind: self.window.BindMLineEdit.setText(keybind))
        self.k_bindWindow.keybindSignal.connect(lambda keybind: self.window.bindKBLineEdit.setText(keybind))
        self.k_clickWindow.keybindSignal.connect(lambda keybind, _: self.window.clickBindKB.setText(keybind))

    @Slot()
    def m_LeftModeClicked(self):
        self.leftMouseModeButton.setDisabled(True)
        self.rightMouseModeButton.setDisabled(False)
        self.window.modeMLabel.setFocus()

    @Slot()
    def m_RightModeClicked(self):
        self.leftMouseModeButton.setDisabled(False)
        self.rightMouseModeButton.setDisabled(True)
        self.window.modeMLabel.setFocus()

    @Slot()
    def m_BindButton(self):
        self.m_bindWindow.show()

    @Slot()
    def k_BindButton(self):
        self.k_bindWindow.show()

    @Slot()
    def k_ClickerButton(self):
        self.k_clickWindow.show()



