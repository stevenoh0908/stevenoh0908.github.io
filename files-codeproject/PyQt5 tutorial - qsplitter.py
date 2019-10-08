#PyQt5 Tutorial - QSplitter
'''
스플리터(Splitter)는 경계를 드래그해서 자식 위젯의 크기를 조절할 수 있도록 해준다
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        hboxlayout = QHBoxLayout()

        topframe = QFrame()
        topframe.setFrameShape(QFrame.Box)

        midleftframe = QFrame()
        midleftframe.setFrameShape(QFrame.StyledPanel)

        midrightframe = QFrame()
        midrightframe.setFrameShape(QFrame.Panel)

        bottomframe = QFrame()
        bottomframe.setFrameShape(QFrame.WinPanel)
        bottomframe.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleftframe)
        splitter1.addWidget(midrightframe)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(topframe)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottomframe)

        hboxlayout.addWidget(splitter2)
        self.setLayout(hboxlayout)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
