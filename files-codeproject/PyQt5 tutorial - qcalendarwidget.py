#PyQt5 Tutorial - QCalendarWidget

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        calendar = QCalendarWidget(self)
        calendar.setGridVisible(True)
        calendar.clicked[QDate].connect(self.showDate)

        self.label = QLabel(self)
        date = calendar.selectedDate()
        self.label.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(calendar)
        vbox.addWidget(self.label)
        
        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()
        pass

    def showDate(self, date):
        self.label.setText(date.toString())
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
