#PyQt5 Tutorial - QColorDialog

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        color = QColor(0, 0, 0)

        self.button = QPushButton('Dialog', self)
        self.button.move(30, 30)
        self.button.clicked.connect(self.showDialog)

        self.frame = QFrame(self)
        self.frame.setStyleSheet('QWidget { background-color:%s }' % color.name())
        self.frame.setGeometry(150, 35, 100, 100)

        self.setWindowTitle('Color Dialog')
        self.setGeometry(300, 300, 300, 180)
        self.show()
        pass

    def showDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.frame.setStyleSheet('QWidget { background-color: %s }' % color.name())
            pass
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
