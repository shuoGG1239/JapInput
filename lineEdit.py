from PyQt5.QtWidgets import QLineEdit


class LineEdit(QLineEdit):
    def __init__(self, parent):
        super(QLineEdit, self).__init__(parent)
        self.setMaxLength(20)


    def isLonger(self, text):
        return len(text) > len(self.text())
