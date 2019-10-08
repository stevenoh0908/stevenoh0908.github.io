#PyQt5 Tutorial - Absolute Positioning
#각 위젯의 위치와 크기를 픽셀 단위로 설정하여 배치.
#제약: 창의 크기를 조절해도 위젯의 크기 및 위치는 변하지 않음
#다양한 플랫폼에서 어플리케이션이 다르게 보일 수 있음
#폰트 바꾸면 레이아웃이 망가질 수 있음
#레이아웃 바꾸고 싶으면 완전히 새로 고쳐야 하며 매우 번거로움

#좌표계는 왼쪽 상단 모서리에서 시작, x좌표는 Left ->Right, y좌표는 Top->Bottom

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        button1 = QPushButton('Button1', self)
        button1.move(80, 13)
        button2 = QPushButton('Button2', self)
        button2.move(80, 53)

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        pass
    pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
