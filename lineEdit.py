from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt, pyqtSignal


class LineEdit(QLineEdit):
    sgnDownPress = pyqtSignal()

    def __init__(self, parent):
        super(QLineEdit, self).__init__(parent)
        self.setMaxLength(20)

    def isLonger(self, text):
        return len(text) > len(self.text())

    def keyPressEvent(self, e):
        if (e.key() == Qt.Key_Down):
            self.sgnDownPress.emit()
        super().keyPressEvent(e)
