from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QSize


class ListWidget(QListWidget):
    sgnAddItem = pyqtSignal(QListWidgetItem)
    sgnClearItem = pyqtSignal()
    sgnEnterItem = pyqtSignal(QListWidgetItem)
    sgnTopupItem = pyqtSignal()

    def __init__(self, parent):
        super(QListWidget, self).__init__(parent)

    def addItem(self, *__args):
        super().addItem(*__args)
        self.sgnAddItem.emit(__args[0])

    def clear(self):
        super().clear()
        self.sgnClearItem.emit()

    def newItem(self, text):
        newItem = QListWidgetItem()
        newItem.setSizeHint(QSize(100, 50))
        newItem.setText(text)
        return newItem

    def addTextItems(self, texts):
        for t in texts:
            self.addItem(self.newItem(t))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.sgnEnterItem.emit(self.currentItem())
        if e.key() == Qt.Key_Up and self.currentRow() == 0:
            self.sgnTopupItem.emit()
        super().keyPressEvent(e)
