#PyQt5 Tutorial - QTextEdit

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.label1 = QLabel('Enter your sentence:')
        self.textedit = QTextEdit()
        self.textedit.setAcceptRichText(False)
        self.label2 = QLabel('The number of words is 0')

        self.textedit.textChanged.connect(self.text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.textedit)
        vbox.addWidget(self.label2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def text_changed(self):
        text = self.textedit.toPlainText()
        self.label2.setText('The number of words is ' + str(len(text.split())))
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
 