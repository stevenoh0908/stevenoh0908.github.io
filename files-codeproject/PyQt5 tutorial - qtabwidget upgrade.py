#PyQt5 Tutorial - QTabWidget Upgrade

import sys
from PyQt5.QtWidgets import *

class MyApp(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass
    
    def initUI(self):
        tabs = QTabWidget()
        tabs.addTab(FirstTab(), 'First')
        tabs.addTab(SecondTab(), 'Second')
        tabs.addTab(ThirdTab(), 'Thrid')

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()
        pass
    pass

class FirstTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        name = QLabel('Name:')
        nameedit = QLineEdit()
        age = QLabel('Age:')
        ageedit = QLineEdit()
        nation = QLabel('Nation:')
        nationedit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(name)
        vbox.addWidget(nameedit)
        vbox.addWidget(age)
        vbox.addWidget(ageedit)
        vbox.addWidget(nation)
        vbox.addWidget(nationedit)

        self.setLayout(vbox)
        pass
    pass

class SecondTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        lan_group = QGroupBox('Select Your Language')
        combo = QComboBox()
        list = ['Korean', 'English', 'Chinese']
        combo.addItems(list)

        vbox = QVBoxLayout()
        vbox.addWidget(combo)
        lan_group.setLayout(vbox)

        learn_group = QGroupBox('Select What You Want To Learn')
        korean = QCheckBox('Korean')
        english = QCheckBox('English')
        chinese = QCheckBox('Chinese')

        vbox1 = QVBoxLayout()
        vbox1.addWidget(korean)
        vbox1.addWidget(english)
        vbox1.addWidget(chinese)
        learn_group.setLayout(vbox1)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(lan_group)
        vbox.addWidget(learn_group)
        self.setLayout(vbox2)
        pass
    pass

class ThirdTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        label = QLabel('Terms and Conditions')
        text_browser = QTextBrowser()
        text_browser.setText('This is the terms and conditions')
        checkbox = QCheckBox('Check the terms and conditions')

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(text_browser)
        vbox.addWidget(checkbox)

        self.setLayout(vbox)
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
