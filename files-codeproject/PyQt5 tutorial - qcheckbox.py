#PyQt5 Tutorial - QCheckBox
'''
자주 쓰이는 메서드
text() 체크 박스의 라벨 텍스트 반환
setText() 체크 박스의 라벨 텍스트 설정
isChecked() 체크 박스의 상태 반환. True/False
checkState() 체크 박스의 상태 반환(2: 체크/1: 변경 없음/0: 해제)
toggle() 체크 박스의 상태 변경

자주 쓰이는 시그널
pressed() 체크 박스를 누를 때 발생
released() 체크 박스에서 뗄 때 발생
clicked() 체크 박스 클릭할 때 발생
stateChanged() 체크 박스 상태가 바뀔 때 발생'
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        checkbox = QCheckBox('Show Title', self)
        checkbox.move(20, 20)
        checkbox.toggle()
        checkbox.stateChanged.connect(self.changeTitle)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
            pass
        else:
            self.setWindowTitle(' ')
            pass
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass

