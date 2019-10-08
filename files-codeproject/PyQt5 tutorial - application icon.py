#PyQt5 Tutorial - Application Icon

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.setWindowTitle("Icon Example")
        self.setWindowIcon(QIcon("web.png"))
        #QWidget.setWindowIcon(QIcon("filedir")): set window icon to object using by QIcon class in filedir
        self.setGeometry(300, 300, 300, 200)
        #QWidget.setGeometry(x, y, width, height): set window geometry. move to (x, y) and set size to (width, height). px unit.
        self.show()
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
