#PyQt5 Tutorial - Menubar
#macOS에서는 특별히 menubar.setNativeMenuBar(False)를 추가해주어야 함

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        #QAction(Icon 객체, Text, Master)
        exitAction.setShortcut('Ctrl+Q')
        #QAction.setShortcut('shortcut text')
        exitAction.setStatusTip('Exit Application')
        #QAction.setStatusTip('Tip text')
        exitAction.triggered.connect(qApp.quit)
        #QAction.triggered 시그널을 QApp.quit 메서드에 connect.

        self.statusBar()

        menubar = self.menuBar()
        #QMainWindow의 menuBar 객체 호출
        menubar.setNativeMenuBar(False)
        #MacOS 호환용 지시
        fileMenu = menubar.addMenu('&File')
        #메뉴바의 메뉴 생성 menubar.addMenu('MenuName'): 이름 앞 &(ampersand)는 단축키 간편 설정: F 앞에 앰퍼샌드가 있어서 Alt+F의 단축키
        fileMenu.addAction(exitAction)
        #fileMenu에 Action 추가

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass

        
