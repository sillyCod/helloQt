# -*- coding: utf-8 -*-
# time: 19-3-7 上午11:30
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPushButton, QHBoxLayout, QWidget, QToolTip
from PyQt5.QtGui import QIcon, QFont


class TestMain(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(400, 200)
        self.status = self.statusBar()
        self.status.showMessage("这是一个状态栏", 5000)
        self.setWindowTitle("这是关闭窗口的例子")
        self.closeBtn = QPushButton("关闭")
        self.closeBtn.clicked.connect(self.onBtnClicked)
        layout = QHBoxLayout()
        layout.addWidget(self.closeBtn)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)
        self.initUI()
        self.center()

    def center(self):
        geometry = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((geometry.width()-size.width())/2, (geometry.height()-size.height())/2)

    def onBtnClicked(self):
        sender = self.sender()
        print(sender.text(), "被按下了")
        app = QApplication.instance()
        app.quit()

    def initUI(self):
        self.setToolTip("这是一个<br>气泡提示</br>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./cartoon1.ico"))
    ui = TestMain()
    ui.show()
    sys.exit(app.exec())
