import japInput
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWindow = japInput.JapInput()
    mainWindow.setAttribute(Qt.WA_TranslucentBackground, True)
    mainWindow.setWindowFlags(Qt.FramelessWindowHint)
    mainWindow.setStyleSheet('QWidget{color:black}')
    mainWindow.show()
    sys.exit(app.exec_())
