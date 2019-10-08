#PyQt5 Tutorial - QComboBox

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.label = QLabel('Option1', self)
        self.label.move(50, 150)

        comboBox = QComboBox(self)
        comboBox.addItem('Option1')
        comboBox.addItem('Option2')
        comboBox.addItem('Option3')
        comboBox.addItem('Option4')
        comboBox.move(50, 50)

        comboBox.activated[str].connect(self.onActivated)

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def onActivated(self, text):
        self.label.setText(text)
        self.label.adjustSize()
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass


