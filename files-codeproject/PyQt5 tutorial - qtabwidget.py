#PyQt5 Tutorial - QTabWidget

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):

        tab1 = QWidget()
        tab2 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
