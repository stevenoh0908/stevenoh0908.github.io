#PyQt5 Tutorial - Signal and Slot: Reconstruct event handler
'''
자주 사용되는 이벤트 핸들러
keyPressEvent 키보드를 눌렀을 때 발생
keyReleaseEvent 키보드를 눌렀다가 뗄 때 발생
mouseDoubleClickEvent 마우스를 더블클릭할 때 발생
mouseMoveEvent 마우스를 움직일 때 발생
mousePressEvent 마우스를 누를 때 발생
mouseReleaseEvent 마우스를 눌렀다가 뗄 때 발생
moveEvent 위젯이 이동할 때 동작
resizeEvent 위젯의 크기를 변경할 때 동작
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
            pass
        elif event.key() == Qt.Key_F:
            self.showFullScreen()
            pass
        elif event.key() == Qt.Key_N:
            self.showNormal()
            pass
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
