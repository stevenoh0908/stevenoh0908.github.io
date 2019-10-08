#PyQt5 Tutorial - Displaying Time and Date
#QDate Class는 날짜와 관련된 기능의 제공, QTime Class는 시간과 관련된 기능의 제공

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QDateTime

#QDate
now = QDate.currentDate()
print(now.toString())
print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('ddd.MMMM.yyyy'))
print(now.toString('yyyy.MM.dd'))
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

#QTime
time = QTime.currentTime()
print(time.toString())
print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString('hh.mm.ss.zzz'))
print(time.toString(Qt.DefaultLocaleLongDate))
print(time.toString(Qt.DefaultLocaleShortDate))

#QDateTime
datetime = QDateTime.currentDateTime()
print(datetime.toString())
print(datetime.toString('d.MM.yy hh:mm:ss'))
print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print(datetime.toString(Qt.DefaultLocaleShortDate))

#Displaying date on status bar
class MyApp(QMainWindow):

    def __init__(self):

        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()
        pass

    def initUI(self):

        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleShortDate))
        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        pass

    pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass

