from typing import Literal
from db import get_config
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QKeyEvent, QKeySequence
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class KeyBindWindow(QWidget):
    keybindSignal = Signal(str)
    keybindReset = Signal()

    def __init__(self, mode: Literal['mouse', 'keyboard', None]):
        super().__init__()
        self.keybind = ''
        self.mode: Literal['mouse', 'keyboard'] = mode

        self.setWindowTitle("Bind de Tecla")
        self.setGeometry(300, 200, 400, 200)

        layout = QVBoxLayout(self)

        self.message_label = QLabel("Pressione a tecla de ativação/desativação!", self)
        self.message_label.setStyleSheet('font-size: 18px;')
        self.message_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.message_label)

        self.line_edit = QLineEdit(self)
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.line_edit.setStyleSheet('font-size: 26px;')
        self.line_edit.setContextMenuPolicy(Qt.NoContextMenu)
        self.line_edit.setReadOnly(True)
        layout.addWidget(self.line_edit)

        button_layout = QHBoxLayout()
        self.cancel_button = QPushButton("Cancelar", self)
        self.cancel_button.setFocusPolicy(Qt.NoFocus)
        button_layout.addWidget(self.cancel_button)

        self.reset_button = QPushButton("Resetar /\nDesabilitar", self)
        self.reset_button.setFocusPolicy(Qt.NoFocus)
        button_layout.addWidget(self.reset_button)

        self.confirm_button = QPushButton("Confirmar", self)
        self.confirm_button.setFocusPolicy(Qt.NoFocus)
        button_layout.addWidget(self.confirm_button)

        layout.addLayout(button_layout)

        self.cancel_button.clicked.connect(self.close)
        self.reset_button.clicked.connect(self.reset_keybind)
        self.confirm_button.clicked.connect(self.confirm_key)
        self.setWindowModality(Qt.ApplicationModal)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if bool(event.text().strip()):  # Se a tecla não for um espaço/inválida
            self.line_edit.setText(event.text().upper())
        return event.ignore()

    @Slot()
    def confirm_key(self):
        if bool(self.line_edit.text().strip()):
            config = get_config()
            self.keybind = self.line_edit.text().upper().strip()
            if self.mode == 'mouse':
                if config['keyboard']['bind'] == self.keybind.lower():
                    return self.error_duplicated_bind('teclado')
            if self.mode == 'keyboard':
                if config['mouse']['bind'] == self.keybind.lower():
                    return self.error_duplicated_bind('mouse')
            self.close()
            self.keybindSignal.emit(self.keybind)
        else:
            self.msgbox = QMessageBox(self)
            self.msgbox.setWindowTitle('ERRO!')
            self.msgbox.setText('A tecla inserida não é válida!\nTente novamente com outra tecla!')
            self.msgbox.setStyleSheet('font-size: 15px; text-align: right;')
            self.msgbox.setIcon(QMessageBox.Icon.Critical)
            self.msgbox.show()

    def error_duplicated_bind(self, mode_text: str):
        self.msgbox = QMessageBox(self)
        self.msgbox.setWindowTitle('ERRO!')
        self.msgbox.setText(f'A tecla inserida já está sendo utilizada como bind do {mode_text}!\nTente novamente com outra tecla!')
        self.msgbox.setStyleSheet('font-size: 15px; text-align: right;')
        self.msgbox.setIcon(QMessageBox.Icon.Critical)
        self.msgbox.show()

    @Slot()
    def reset_keybind(self):
        self.line_edit.clear()
        self.keybind = ''
        self.keybindReset.emit()
        self.close()

class KeyClickerWindow(KeyBindWindow):
    keybindSignal = Signal(str, str)  # key_friendly_text, key_code

    def __init__(self):
        super().__init__(None)
        self.key = None

        self.setWindowTitle("Seleção de Tecla")
        self.layout().removeWidget(self.message_label)
        self.message_label.deleteLater()
        self.message_label = QLabel("Pressione a tecla que será repetida automaticamente!", self)
        self.message_label.setStyleSheet('font-size: 17px; text-align: center;')
        self.message_label.setAlignment(Qt.AlignCenter)
        self.layout().insertWidget(0, self.message_label)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        match event.key():
            case Qt.Key.Key_Space:
                keyText = 'ESPAÇO'
            case Qt.Key.Key_Up:
                keyText = 'SETA ↑'
            case Qt.Key.Key_Down:
                keyText = 'SETA ↓'
            case Qt.Key.Key_Left:
                keyText = 'SETA ←'
            case Qt.Key.Key_Right:
                keyText = 'SETA →'
            case Qt.Key.Key_Return:
                keyText = 'ENTER'
            case _:
                keyText = QKeySequence(event.key()).toString()

        self.line_edit.setText(keyText.upper())
        self.key = QKeySequence(event.key()).toString()
        return event.ignore()

    @Slot()
    def confirm_key(self):
        if bool(self.line_edit.text().strip()):
            self.keybind = self.line_edit.text().upper()
            self.close()
            self.keybindSignal.emit(self.keybind, self.key)
        else:
            self.msgbox = QMessageBox(self)
            self.msgbox.setWindowTitle('ERRO!')
            self.msgbox.setText('A tecla inserida não é válida!\nTente novamente com outra tecla!')
            self.msgbox.setIcon(QMessageBox.Icon.Critical)
            self.msgbox.show()
