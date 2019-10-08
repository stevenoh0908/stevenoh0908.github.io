#PyQt5 Tutorial - Signal and Slot: Another Reconstruct Event Handler

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        x = y = 0
        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(20, 20)

        self.setMouseTracking(True)

        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()

        text = 'x: {0}, y: {1}'.format(x, y)
        self.label.setText(text)
        self.label.adjustSize()
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
