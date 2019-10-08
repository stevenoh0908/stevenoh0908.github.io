#PyQt5 Tutorial - QTextBrowser(upgrade)

import sys
from PyQt5.QtWidgets import *
import requests
from bs4 import BeautifulSoup

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText('Enter your search word')
        self.lineedit.returnPressed.connect(self.crawl_news)
        
        self.button = QPushButton('Search')
        self.button.clicked.connect(self.crawl_news)

        self.label = QLabel('')
        
        self.textbrowser = QTextBrowser()
        self.textbrowser.setAcceptRichText(True)
        self.textbrowser.setOpenExternalLinks(True)

        gridlayout = QGridLayout()
        gridlayout.addWidget(self.lineedit, 0, 0, 1, 3)
        gridlayout.addWidget(self.button, 0, 3, 1, 1)
        gridlayout.addWidget(self.label, 1, 0, 1, 4)
        gridlayout.addWidget(self.textbrowser, 2, 0, 1, 4)

        self.setLayout(gridlayout)

        self.setWindowTitle('Web Crawler')
        self.setGeometry(100, 100, 700, 450)
        self.show()
        pass

    def crawl_news(self):
        search_word = self.lineedit.text()

        if search_word:
            self.label.setText('BBC Search Results for "' + search_word + '"')
            self.textbrowser.clear()

            url_search = 'https://www.bbc.co.uk/search?q='
            url = url_search + search_word

            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')

            titles_html = soup.select('.search-results > li > article > div > h1 > a')

            for i in range(len(titles_html)):
                title = titles_html[i].text
                link = titles_html[i].get('href')
                self.textbrowser.append(str(i+1)+'. ' +title+' (<a href="'+link+'">Link</a>'+')')
                pass
            pass
        pass
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    pass
