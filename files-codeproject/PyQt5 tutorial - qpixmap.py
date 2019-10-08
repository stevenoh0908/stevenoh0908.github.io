#PyQt5 Tutorial - QPixmap
'''
QPixmap 지원 Image 파일 형식
bmp Read/Write
gif Read
jpg Read/Write
jpeg Read/Write
png Read/Write
pbm Read
pgm Read
ppm Read/Write
xbm Read/Write
xpm Read/Write
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        pixmap = QPixmap('landscape.jpg')

        label_image = QLabel()
        label_image.setPixmap(pixmap)
        label_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        label_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(label_image)
        vbox.addWidget(label_size)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
