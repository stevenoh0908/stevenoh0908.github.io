#PyQt5 Tutorial - QInputDialog
'''
자주 사용하는 메서드
getText()
getMultiLineText()
getInt()
getDouble()
getItem()
'''

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.button = QPushButton('Dialog', self)
        self.button.move(30, 30)
        self.button.clicked.connect(self.showDialog)

        self.lineedit = QLineEdit(self)
        self.lineedit.move(150, 33)

        self.setWindowTitle('Input Dialog')
        self.setGeometry(400, 300, 400, 200)
        self.show()
        pass

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.lineedit.setText(str(text))
            pass
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
