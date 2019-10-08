#PyQt5 Tutorial - QDoubleSpinBox

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.label1 = QLabel('QDoubleSpinBox')
        self.doublespinbox = QDoubleSpinBox()
        self.doublespinbox.setRange(0, 100)
        self.doublespinbox.setSingleStep(0.5)
        self.doublespinbox.setPrefix('$ ')
        self.doublespinbox.setDecimals(1)
        self.label2 = QLabel('$ 0.0')
        
        self.doublespinbox.valueChanged.connect(self.value_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.doublespinbox)
        vbox.addWidget(self.label2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDoubleSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def value_changed(self):
        self.label2.setText('$ '+str(self.doublespinbox.value()))
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
