#PyQt5 Tutorial - QRadioButton
'''
자주 쓰이는 메서드
text() 버튼의 텍스트 반환
setText() 버튼의 텍스트 설정
setChecked() 버튼의 선택 여부 결정
isChecked() 버튼의 선택 여부 반환
toggle() 버튼의 상태 변경
setAutoExclusive() 한 위젯 내에서 라디오 버튼을 하나의 그룹으로 묶음(True/False)

자주 쓰이는 시그널
pressed() 버튼을 누를 때 발생
released() 버튼을 땔 때 발생
clicked() 버튼을 클릭할 때 발생
toggled() 버튼의 상태가 바뀔 때 발생
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass
    
    def initUI(self):
        radiobutton1 = QRadioButton('First Button', self)
        radiobutton1.move(50, 50)
        radiobutton1.setChecked(True)
        
        radiobutton2 = QRadioButton(self)
        radiobutton2.move(50, 70)
        radiobutton2.setText('Second Button')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
