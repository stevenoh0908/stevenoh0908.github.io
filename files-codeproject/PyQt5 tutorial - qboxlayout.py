#PyQt5 Tutorial - Box Layout
#QHBoxLayout: 수평 박스 정렬 레이아웃
#QVBoxLayout: 수직 박스 정렬 레이아웃

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        #QBoxLayout에서 공간 확보 메서드는 addStretch(cells to stretch)
        hbox.addWidget(okButton)
        hbox.addStretch(1)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
