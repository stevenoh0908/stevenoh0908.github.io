#PyQt5 tutorial - open window

import sys
from PyQt5.QtWidgets import QApplication, QWidget
#PyQt에서 기본적인 UI 구성 요소들을 제공하는 Widget은 대부분 PyQt5.QtWidgets 모듈에 포함됨

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.setWindowTitle("Test Application")
        #QWidget.setWindowTitle("string") : set widget's title to "string"
        self.move(300, 300)]
        #QWidget.move(x, y) : set widget's position in the screen to x(px) and y(px)
        self.resize(400, 200)
        #QWidget.resize(width, height): set widget's size to width X height(px)
        self.show()
        #QWidget.show(): Show Widget to Screen
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #모든 PyQt5 Application은 어플리케이션 객체를 생성해야 한다.
    ex = MyApp()
    sys.exit(app.exec_())
    pass
