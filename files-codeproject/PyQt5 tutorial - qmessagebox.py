#PyQt5 Tutorial - QMessageBox

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.setWindowTitle('QMessageBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            pass

        else:
            event.ignore()
            pass
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
