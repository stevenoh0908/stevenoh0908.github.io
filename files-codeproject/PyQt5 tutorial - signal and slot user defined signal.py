#PyQt5 Tutorial - Signal and Slot: User Defined Signal

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import *

class Communicate(QObject):
    closeApp = pyqtSignal()
    pass

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.communicate = Communicate()
        self.communicate.closeApp.connect(self.close)
        
        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def mousePressEvent(self, event):
        self.communicate.closeApp.emit()
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
