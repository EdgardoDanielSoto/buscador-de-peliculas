# main.py

from PySide6.QtWidgets import QApplication, QWidget
from ui.ventana_principal import Ui_ventana_principal

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_ventana_principal()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
