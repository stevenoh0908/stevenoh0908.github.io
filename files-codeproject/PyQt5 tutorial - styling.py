#PyQt5 Tutorial - Styling
#스타일 시트는 html css로 처리하면 됨

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        label_red = QLabel('Red')
        label_green = QLabel('Green')
        label_blue = QLabel('Blue')

        label_red.setStyleSheet("color: red; border-style: solid; border-width: 2px; border-color: #FA8072; border-radius: 3px")
        label_green.setStyleSheet("color: green; background-color: #7FFFD4")
        label_blue.setStyleSheet("color: blue; background-color: #87CEFA; border-style: dashed; border-width: 3px; border-color: #1E90FF")

        vbox = QVBoxLayout()
        vbox.addWidget(label_red)
        vbox.addWidget(label_green)
        vbox.addWidget(label_blue)

        self.setLayout(vbox)

        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass
    pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
