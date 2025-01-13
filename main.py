import os
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from main_window import MainWindow
from qt_material import apply_stylesheet

def get_resource(file):  # necessario para obter arquivos apos pyinstaller
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, file)

def main():
    app = QApplication()

    window = MainWindow()

    apply_stylesheet(app, theme='dark_blue.xml', css_file=get_resource('custom.css'))
    icon = QIcon(get_resource("logo.ico"))
    window.setWindowIcon(icon)

    if sys.platform.startswith('win'):  # fix para icone funcionar em windows
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')

    window.show()
    app.exec()

if __name__ == '__main__':
    main()
