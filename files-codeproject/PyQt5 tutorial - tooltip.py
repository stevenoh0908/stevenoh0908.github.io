#PyQt5 Tutorial - Tooltip
#툴팁은 어떤 위젯의 기능을 설명하는 등의 역할을 하는 말풍선 형태의 도움말로서,
#위젯에 있는 모든 구성 요소에 대하여 tooltip의 삽입이 가능함

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        #QToolTip.setFont(QFont('fontname', fontsize))
        self.setToolTip('This is a <b>QWidget</b> widget')
        #구성요소.setToolTip("Text"). 웬만한 Text 속성에는 html 문법을 사용 가능하다
        button = QPushButton("Button", self)
        button.setToolTip("This is a <b>QPushButton</b> widget")
        button.move(50, 50)
        button.resize(button.sizeHint())
        #Button.resize(Button.sizeHint()): 버튼을 적절한 크기로 Resizing

        self.setWindowTitle("Tooltips")
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
