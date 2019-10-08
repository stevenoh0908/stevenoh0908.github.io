#PyQt5 Tutorial - QSlider & QDial
'''
QSlider
자주 사용되는 메서드
setTickInterval() 슬라이더 tick 간격 조절
setTickPosition() 슬라이더 tick 위치 조절
-> setTickPosition()에서 아래의 값을 사용
-> QSlider.NoTicks : 틱 표시 X
-> QSlider.TicksAbove : 틱을 수평 슬라이더 위쪽에 표시
-> QSlider.TicksBelow : 틱을 수평 슬라이더 아래쪽에 표시
-> QSlider.TicksBothSides : 틱을 수평 슬라이더 양쪽에 표시
-> QSlider.TicksLeft : 틱을 수직 슬라이더 왼쪽에 표시
-> QSlider.TicksRight : 틱을 수직 슬라이더 오른쪽에 표시

QDial
자주 사용되는 메서드
setNotchesVisible() True/False 다이얼 위젯에 노치 표시의 toggle

QDial & QSlider
자주 사용되는 시그널
valueChanged() 슬라이더의 값이 변할 때 발생
sliderPressed() 슬라이더를 움직이기 시작할 때 발생
sliderMoved() 슬라이더를 움직이면 발생
sliderReleased() 슬라이더를 놓을 때 발생
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)

        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)

        button = QPushButton('Default', self)
        button.move(35, 160)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        button.clicked.connect(self.button_clicked)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        pass

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
