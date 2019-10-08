#PyQt5 Tutorial - QFileDialog

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def showDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', './')

        if filename[0]:
            file = open(filename[0], 'r')
            with file:
                data = file.read()
                self.textEdit.setText(data)
                pass
            pass
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
