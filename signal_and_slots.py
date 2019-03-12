# -*- coding: utf-8 -*-
# time: 19-3-11 下午5:29
from PyQt5.QtCore import QObject, pyqtSignal, QMetaObject


class Signal(QObject):
    send_msg = pyqtSignal(object)

    def run(self):
        self.send_msg.emit("hello")


class Slot(QObject):

    def get(self, msg):
        print("called")
        print(msg)


if __name__ == "__main__":
    signal = Signal()
    slot = Slot()
    signal.send_msg.connect(slot.get)
    signal.run()
