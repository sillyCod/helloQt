# -*- coding: utf-8 -*-
# time: 19-3-1 下午1:58
# !/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow  # 导入相应的包
from HelloWorld import *


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建QApplication对象是必须，管理整个程序，参数可有可无，有的话可接收命令行参数
    window = MainWindow()
    window.show()


    # w = QWidget()  # 创建窗体对象，
    # w.resize(250, 150)  # 设置窗体大小
    # w.move(100, 300)  # 设置在屏幕上的显示位置
    # w.setWindowTitle('Hello, PyQt')  # 设置窗口标题
    # w.show()  # 窗口显示

    sys.exit(app.exec_())
