#PyQt5 Tutorial - Toolbar
#Toolbar는 자주 사용하는 명령들을 편리하게 사용 가능하게 해 주는 객체

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
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        #QMainWindow의 툴바를 추가
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass

        
