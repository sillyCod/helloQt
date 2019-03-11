# -*- coding: utf-8 -*-
# time: 19-3-7 下午2:35

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette, QPixmap


class LabelDemo(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1000, 1000)
        self.initUi()

    def initUi(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("这是文本标签label1")
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("./python.jpg"))

        label4.setText("<a href='https://www.douban.com/'>这是一个超链接标签</a>")
        label4.setToolTip("这是一个超链接标签")
        label4.setAlignment(Qt.AlignRight)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        label1.setOpenExternalLinks(True)
        label4.setOpenExternalLinks(False)

        label4.linkActivated.connect(link_clicked)

        label2.linkHovered.connect(link_hovered)

        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)


def link_clicked():
    print("链接被点击了")


def link_hovered():
    print("链接hovered")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = LabelDemo()
    ui.show()
    sys.exit(app.exec())
