#PyQt5 Tutorial - QTimeEdit

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        label = QLabel('QTimeEdit')

        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        timeedit.setDisplayFormat('hh:mm:ss')

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(timeedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
