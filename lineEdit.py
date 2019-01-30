from PyQt5.QtWidgets import QLineEdit


class LineEdit(QLineEdit):
    def __init__(self, parent):
        super(QLineEdit, self).__init__(parent)
