#PyQt5 Tutorial - Grid Layout
#Grid Layout에서는 위젯의 공간을 행(row)과 열(column)으로 구분함
#그리드 레이아웃은 QGridLayout Class

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QTextEdit, QLabel

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        #QGridLayout.addWidget(object, row, column)
        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
