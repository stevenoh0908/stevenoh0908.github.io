#PyQt5 Tutorial - Widget: QPushButton
'''
자주 사용되는 메서드
setCheckable() true 설정시 누른 상태와 그렇지 않은 상태를 구분함
toggle() 상태를 변경
setIcon() 버튼 아이콘 설정
setEnabled() False 설정 시, 버튼 사용 불능
isChecked() 버튼의 선택 여부를 반환
setText() 버튼 표시 텍스트를 설정
text() 버튼 표시 텍스트 반환

자주 사용되는 시그널
clicked() 버튼 클릭시 발생
pressed() 버튼이 눌렸을 때 발생
released() 버튼을 눌렀다 땔 때에 발생
toggled() 버튼의 상태가 바뀔 때 발생
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):

        button1 = QPushButton('&Button1', self)
        button1.setCheckable(True)
        button1.toggle()

        button2 = QPushButton('&Button2', self)
        button2.setCheckable(True)
        
        button3 = QPushButton('Button3', self)
        button3.setCheckable(False)

        vbox = QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass