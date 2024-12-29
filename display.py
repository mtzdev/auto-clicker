from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class KeyBindWindow(QWidget):
    keybindSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.keybind = ''

        self.setWindowTitle("Bind de Tecla")
        self.setGeometry(300, 200, 400, 200)

        layout = QVBoxLayout(self)

        self.message_label = QLabel("Pressione uma tecla para a bind.", self)
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
        self.confirm_button = QPushButton("Confirmar", self)

        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.confirm_button)

        layout.addLayout(button_layout)

        self.cancel_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.confirm_key)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if bool(event.text().strip()):  # Se a tecla não for um espaço/inválida
            self.line_edit.setText(event.text().upper())
        return event.ignore()

    def confirm_key(self):
        if bool(self.line_edit.text().strip()):
            self.keybind = self.line_edit.text().upper()
            self.close()
            self.keybindSignal.emit(self.keybind)
        else:
            self.msgbox = QMessageBox(self)
            self.msgbox.setWindowTitle('ERRO!')
            self.msgbox.setText('Não é possível salvar sua bind pois não é uma tecla válida!')
            self.msgbox.setIcon(QMessageBox.Icon.Critical)
            self.msgbox.show()
