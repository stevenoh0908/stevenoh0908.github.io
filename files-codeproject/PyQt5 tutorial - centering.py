#PyQt5 Tutorial - Move Screen To Center(Centering)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class MyApp(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        pass

    def initUI(self):

        self.setWindowTitle('Centering The Screen')
        self.resize(500, 350)
        self.center()
        self.show()
        pass

    def center(self):
        qr = self.frameGeometry()
        #QWidget.frameGeometry(): 창의 위치와 크기 정보 get
        cp = QDesktopWidget().availableGeometry().center()
        #QDesktopWidget().availableGeometry().center(): 모니터 화면의 가운데 위치 return
        qr.moveCenter(cp)
        #QWidget.frameGeometry.moveCenter(Geometry Information): 해당 위젯의 frameGeometry를 Info로 set
        self.move(qr.topLeft())
        #QWidget.frameGeometry.topLeft(): 해당 위젯의 topLeft 위치 튜플로 반환
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
