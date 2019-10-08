#PyQt5 Tutorial - QSpinBox

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.label1 = QLabel('QSpinBox')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(30)
        #or self.spinbox.setRange(-10, 30)
        self.spinbox.setSingleStep(2)
        self.label2 = QLabel('0')

        self.spinbox.valueChanged.connect(self.value_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.label2)
        vbox.addStretch()

        self.setLayout(vbox)
        
        self.setWindowTitle('QSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def value_changed(self):
        self.label2.setText(str(self.spinbox.value()))
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
