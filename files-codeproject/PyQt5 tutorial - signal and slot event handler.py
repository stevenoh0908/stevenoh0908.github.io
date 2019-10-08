#PyQt5 Tutorial - Signal and Slot: Event Handler

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        button1 = QPushButton('Big', self)
        button2 = QPushButton('Small', self)

        hbox = QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)
        button1.clicked.connect(self.resizeBig)
        button2.clicked.connect(self.resizeSmall)

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(200, 200, 200, 250)
        self.show()
        pass

    def resizeBig(self):
        self.resize(400, 500)
        pass

    def resizeSmall(self):
        self.resize(200, 250)
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
