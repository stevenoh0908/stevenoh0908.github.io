#PyQt5 Tutorial - Status Bar
#QMainWindow는 메뉴바, 툴바, 상태바를 가지는 전형적인 어플리케이션.
#http://codetorial.net/basics/statusbar.html
#메인 창은 QMenuBar, QToolBar, QDockWidget, QStatusBar 레이아웃 가짐.
#가운데에 Central widget 영역 있고, 여기는 anyone.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

#QStatusBar 클래스. 상태바 텍스트 표시를 위해서는 showMessage("Text", time)
#텍스트 제거시 clearMessage()
#텍스트 get은 currentMessage()
#QStatusBar 클래스는 상태바에 표시되는 메세지가 바뀔 때마다 messageChanged() 시그널을 발생

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.statusBar().showMessage("Ready")
        #QMainWindow class의 statusBar() 메서드를 이용하여 상태바 생성. showMessage("Text to show statusbar")
        self.setWindowTitle("Statusbar")
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
