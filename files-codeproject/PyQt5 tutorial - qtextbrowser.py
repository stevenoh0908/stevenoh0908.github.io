#PyQt5 Tutorial - QTextBrowser

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.lineedit = QLineEdit()
        self.lineedit.returnPressed.connect(self.append_text)

        self.textbrowser = QTextBrowser()
        self.textbrowser.setAcceptRichText(True)
        self.textbrowser.setOpenExternalLinks(True)

        self.clear_button = QPushButton('Clear')
        self.clear_button.pressed.connect(self.clear_text)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lineedit, 0)
        vbox.addWidget(self.textbrowser, 1)
        vbox.addWidget(self.clear_button, 2)

        self.setLayout(vbox)
        
        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()
        pass

    def append_text(self):
        text = self.lineedit.text()
        self.textbrowser.append(text)
        self.lineedit.clear()
        pass

    def clear_text(self):
        self.textbrowser.clear()
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
