#PyQt5 Tutorial - QDateTimeEdit

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        label = QLabel('QDateTimeEdit')

        datetimeedit = QDateEdit(self)
        datetimeedit.setDateTime(QDateTime.currentDateTime())
        datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 12, 31, 00, 00, 00))
        datetimeedit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(datetimeedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDateTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
