#PyQt5 Tutorial - QProgressBar
'''
자주 사용되는 메서드
setMinimum() 진행 표시줄의 최소값 설정
setMaximum() 진행 표시줄의 최대값 설정
setRange() 한꺼번에 진행 표시줄의 최대, 최소값 범위 설정
-> 기본값은 0~99
setValue() 진행 표시줄의 상태를 특정 값으로 설정
reset() 진행 표시줄을 초기 상태로 되돌림
-> 진행 표시줄의 최소, 최대를 모두 0으로 설정하면 항상 진행중인 상태로 표시.
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(30, 40, 200, 25)
        
        self.button = QPushButton('Start', self)
        self.button.move(40, 80)
        self.button.clicked.connect(self.doAction)
        
        self.timer = QBasicTimer()
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step += 1
        self.progressbar.setValue(self.step)
        pass

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
            pass
        else:
            self.timer.start(100, self)
            self.button.setText('Stop')
            pass
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
