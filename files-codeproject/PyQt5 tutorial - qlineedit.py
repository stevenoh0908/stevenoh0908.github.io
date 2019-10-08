#PyQt5 Tutorial - QLineEdit
'''
자주 사용되는 상수(at setEchoMode(아래의 상수))
QLineEdit.Normal 입력된 문자의 표시
QLineEdit.NoEcho 문자열 표시 안함. 비밀번호의 글자수도 공개하지 않을 때에 유용
QLineEdit.Password 비밀번호 가림용 문자를 대신 표시
QLineEdit.PasswordEchoOnEdit 입력할 때만 문자 표시, 수정 중에는 다른 문자를 표시

자주 사용되는 메서드
setEchoMode(DisplayMode) 표시 모드를 DisplayMode로 설정
maxLength(num) 입력되는 텍스트의 길이 제한
setValidator() 입력되는 텍스트의 종류 제한
setText() or insert() 텍스트 편집
text() 텍스트 get
displayText() 표시되는 텍스트 get
setSelection(), selectAll() 텍스트 선택
cut() 잘라내기
copy() 복사하기
paste() 붙여넣기

자주 사용되는 시그널
cursorPositionChanged() 커서가 움직일 때 발생
editingFinished() 편집이 끝났을 때(Return/Enter Pressed) 발생
returnPressed() Return/Enter 버튼이 눌릴 때 발생
selectionChanged() 선택 영역이 바뀔 때 발생
textChanged() 텍스트 변경 시 발생
textEdited() 텍스트 편집 시 발생
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel ,QLineEdit

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.label = QLabel(self)
        self.label.move(60, 40)

        lineedit = QLineEdit(self)
        lineedit.move(60, 100)
        lineedit.textChanged[str].connect(self.onChanged)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        pass

    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()
        pass

    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
