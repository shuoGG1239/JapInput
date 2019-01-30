from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QSize


class ListWidget(QListWidget):
    def __init__(self, parent):
        super(QListWidget, self).__init__(parent)

    def addItem(self, *__args):
        super().addItem(*__args)