# -*- coding: utf-8 -*-
# time: 19-3-4 下午5:08
import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget


class WinForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle("WTF")
        quit = QPushButton("关闭", self)
        quit.setGeometry(10, 10, 60, 35)
        quit.setStyleSheet("background-color: red")
        quit.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
