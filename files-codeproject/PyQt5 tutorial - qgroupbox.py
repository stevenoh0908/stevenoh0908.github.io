#PyQt5 Tutorial - QGroupBox

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        gridlayout = QGridLayout()
        gridlayout.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        gridlayout.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        gridlayout.addWidget(self.createNonExclusiveGroup(), 0, 1)
        gridlayout.addWidget(self.createPushButtonGroup(), 1, 1)

        self.setLayout(gridlayout)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 480, 320)
        self.show()
        pass

    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')

        radiobutton1 = QRadioButton('Radio1')
        radiobutton2 = QRadioButton('Radio2')
        radiobutton3 = QRadioButton('Radio3')
        radiobutton1.setChecked(True)

        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(radiobutton1)
        vboxlayout.addWidget(radiobutton2)
        vboxlayout.addWidget(radiobutton3)
        groupbox.setLayout(vboxlayout)

        return groupbox

    def createSecondExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)

        radiobutton1 = QRadioButton('Radio1')
        radiobutton2 = QRadioButton('Radio2')
        radiobutton3 = QRadioButton('Radio3')
        radiobutton1.setChecked(True)

        checkbox = QCheckBox('Independent Checkbox')
        checkbox.setChecked(True)

        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(radiobutton1)
        vboxlayout.addWidget(radiobutton2)
        vboxlayout.addWidget(radiobutton3)
        vboxlayout.addWidget(checkbox)
        vboxlayout.addStretch(1)
        groupbox.setLayout(vboxlayout)

        return groupbox
    
    def createNonExclusiveGroup(self):
        groupbox = QGroupBox('Non-Exclusive Checkboxes')
        groupbox.setFlat(True)

        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)
        tristatebox = QCheckBox('Tri-state Button')
        tristatebox.setTristate(True)

        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(checkbox1)
        vboxlayout.addWidget(checkbox2)
        vboxlayout.addWidget(tristatebox)
        vboxlayout.addStretch(1)
        groupbox.setLayout(vboxlayout)

        return groupbox
    
    def createPushButtonGroup(self):
        groupbox = QGroupBox('Push Buttons')
        groupbox.setCheckable(True)
        groupbox.setCheckable(True)

        pushbutton = QPushButton('Normal Button')
        togglebutton = QPushButton('Toggle Button')
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)
        flatbutton = QPushButton('Flat Button')
        flatbutton.setFlat(True)
        popupbutton = QPushButton('Popup Button')
        
        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')

        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(pushbutton)
        vboxlayout.addWidget(togglebutton)
        vboxlayout.addWidget(flatbutton)
        vboxlayout.addWidget(popupbutton)
        vboxlayout.addStretch(1)
        groupbox.setLayout(vboxlayout)

        return groupbox
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
