# -*- coding: utf-8 -*-
# time: 19-3-7 上午11:10
import sys
from MainWin02 import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow


class ShowDemo(Ui_Form, QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ShowDemo()
    ui.show()
    sys.exit(app.exec_())