#PyQt5 Tutorial - QLineEdit(Upgrade)

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass
    
    def initUI(self):
        #echo_group
        self.echo_group = QGroupBox('Echo')
        self.echo_label = QLabel('Mode:')

        self.echo_combobox = QComboBox()
        self.echo_combobox.addItem('Normal')
        self.echo_combobox.addItem('No Echo')
        self.echo_combobox.addItem('Password')
        self.echo_combobox.addItem('PasswordEchoOnEdit')
        
        self.echo_lineedit = QLineEdit()
        self.echo_lineedit.setPlaceholderText('Placeholder Text')
        self.echo_lineedit.setFocus()

        #validator_group
        self.validator_group = QGroupBox('Validator')
        self.validator_label = QLabel('Type:')

        self.validator_combobox = QComboBox()
        self.validator_combobox.addItem('No validator')
        self.validator_combobox.addItem('Integer validator')
        self.validator_combobox.addItem('Double validator')

        self.validator_lineedit = QLineEdit()
        self.validator_lineedit.setPlaceholderText('Placeholder Text')

        #alignment_group
        self.alignment_group = QGroupBox('Alignment')
        self.alignment_label = QLabel('Type')

        self.alignment_combobox = QComboBox()
        self.alignment_combobox.addItem('Left')
        self.alignment_combobox.addItem('Center')
        self.alignment_combobox.addItem('Right')

        self.alignment_lineedit = QLineEdit()
        self.alignment_lineedit.setPlaceholderText('Placeholder Text')

        #input_mask_group
        self.input_mask_group = QGroupBox('Input mask')
        self.input_mask_label = QLabel('Type:')

        self.input_mask_combobox = QComboBox()
        self.input_mask_combobox.addItem('No mask')
        self.input_mask_combobox.addItem('Phone number')
        self.input_mask_combobox.addItem('ISO date')
        self.input_mask_combobox.addItem('License Key')

        self.input_mask_lineedit = QLineEdit()
        self.input_mask_lineedit.setPlaceholderText('Placeholder Text')

        #access_group
        self.access_group = QGroupBox('Access')
        self.access_label = QLabel('Type:')

        self.access_combobox = QComboBox()
        self.access_combobox.addItem('False')
        self.access_combobox.addItem('True')

        self.access_lineedit = QLineEdit()
        self.access_lineedit.setPlaceholderText('Placeholder Text')

        #activated connect
        self.echo_combobox.activated.connect(self.echo_changed)
        self.validator_combobox.activated.connect(self.validator_changed)
        self.alignment_combobox.activated.connect(self.alignment_changed)
        self.input_mask_combobox.activated.connect(self.input_mask_changed)
        self.access_combobox.activated.connect(self.access_changed)

        #echo_layout
        self.echo_layout = QGridLayout()
        self.echo_layout.addWidget(self.echo_label, 0, 0)
        self.echo_layout.addWidget(self.echo_combobox, 0, 1)
        self.echo_layout.addWidget(self.echo_lineedit, 1, 0, 1, 2)
        self.echo_group.setLayout(self.echo_layout)

        #validator_layout
        self.validator_layout = QGridLayout()
        self.validator_layout.addWidget(self.validator_label, 0, 0)
        self.validator_layout.addWidget(self.validator_combobox, 0, 1)
        self.validator_layout.addWidget(self.validator_lineedit, 1, 0, 1, 2)
        self.validator_group.setLayout(self.validator_layout)

        #alignment_layout
        self.alignment_layout = QGridLayout()
        self.alignment_layout.addWidget(self.alignment_label, 0, 0)
        self.alignment_layout.addWidget(self.alignment_combobox, 0, 1)
        self.alignment_layout.addWidget(self.alignment_lineedit, 1, 0, 1, 2)
        self.alignment_group.setLayout(self.alignment_layout)

        #input_mask_layout
        self.input_mask_layout = QGridLayout()
        self.input_mask_layout.addWidget(self.input_mask_label, 0, 0)
        self.input_mask_layout.addWidget(self.input_mask_combobox, 0, 1)
        self.input_mask_layout.addWidget(self.input_mask_lineedit, 1, 0, 1, 2)
        self.input_mask_group.setLayout(self.input_mask_layout)

        #access_layout
        self.access_layout = QGridLayout()
        self.access_layout.addWidget(self.access_label, 0, 0)
        self.access_layout.addWidget(self.access_combobox, 0, 1)
        self.access_layout.addWidget(self.access_lineedit, 1, 0, 1, 2)
        self.access_group.setLayout(self.access_layout)

        #layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.echo_group, 0, 0)
        self.layout.addWidget(self.validator_group, 1, 0)
        self.layout.addWidget(self.alignment_group, 2, 0)
        self.layout.addWidget(self.input_mask_group, 0, 1)
        self.layout.addWidget(self.access_group, 1, 1)

        self.setLayout(self.layout)

        self.setWindowTitle('Line Editor')
        self.show()
        pass

    def echo_changed(self, index):
        if index == 0:
            self.echo_lineedit.setEchoMode(QLineEdit.Normal)
            pass
        elif index == 1:
            self.echo_lineedit.setEchoMode(QLineEdit.NoEcho)
            pass
        elif index == 2:
            self.echo_lineedit.setEchoMode(QLineEdit.Password)
            pass
        elif index == 3:
            self.echo_lineedit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
            pass
        pass

    def validator_changed(self, index):
        if index == 0:
            self.validator_lineedit.setValidator(None)
            pass
        elif index == 1:
            self.validator_lineedit.setValidator(QIntValidator(-99, 99))
            pass
        elif index == 2:
            double_validator = QDoubleValidator(-999.0, 999.0, 2)
            double_validator.setNotation(QDoubleValidator.StandardNotation)
            self.validator_lineedit.setValidator(double_validator)
            pass
        
        self.validator_lineedit.clear()
        pass

    def alignment_changed(self, index):
        if index == 0:
            self.alignment_lineedit.setAlignment(Qt.AlignLeft)
            pass
        elif index == 1:
            self.alignment_lineedit.setAlignment(Qt.AlignCenter)
            pass
        elif index == 2:
            self.alignment_lineedit.setAlignment(Qt.AlignRight)
            pass
        pass

    def input_mask_changed(self, index):
        if index == 0:
            self.input_mask_lineedit.setInputMask('')
            pass
        elif index == 1:
            self.input_mask_lineedit.setInputMask('000-0000-0000')
            pass
        elif index == 2:
            self.input_mask_lineedit.setInputMask('0000-00-00')
            self.input_mask_lineedit.setText('20191002')
            self.input_mask_lineedit.setCursorPosition(0)
            pass
        elif index == 3:
            self.input_mask_lineedit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA;#')
            pass
        pass

    def access_changed(self, index):
        if index == 0:
            self.access_lineedit.setReadOnly(False)
            pass
        elif index == 1:
            self.access_lineedit.setReadOnly(True)
            pass
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
