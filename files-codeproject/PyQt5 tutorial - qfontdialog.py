#PyQt5 Tutorial - QFontDialog

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        button = QPushButton('Dialog', self)
        button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        button.move(20, 20)
        button.clicked.connect(self.showDialog)

        vbox = QVBoxLayout()
        vbox.addWidget(button)

        self.label = QLabel('The quick brown fox jumps over the lazy dog', self)
        self.label.move(130, 20)

        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.setWindowTitle('Font Dialog')
        self.setGeometry(300, 300, 250, 180)
        self.show()
        pass

    def showDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.label.setFont(font)
            pass
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
