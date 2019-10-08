#PyQt5 Tutorial - Close Window

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        button = QPushButton("Quit", self)
        #QPushButton의 생성자: QPushButton("Text", parent_widget)
        button.move(50, 50)
        button.resize(button.sizeHint())
        button.clicked.connect(QCoreApplication.instance().quit)
        #QPushButton의 clicked 시그널을 QCoreApplication.instance().quit 메서드로 연결
        #발신자와 수신자를 통하여 이루어지는 Communication
        self.setWindowTitle("Quit Button")
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
