from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from qt_material import apply_stylesheet

def main():
    app = QApplication()

    window = MainWindow()

    apply_stylesheet(app, theme='dark_blue.xml', css_file='custom.css')

    window.show()
    app.exec()

if __name__ == '__main__':
    main()
