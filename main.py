import japInput
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = japInput.JapInput()
    mainWindow.setAttribute(Qt.WA_TranslucentBackground, True)
    mainWindow.setWindowFlags(Qt.FramelessWindowHint)
    mainWindow.setWindowTitle('Jap Input')
    mainWindow.setWindowIcon(QIcon('assert/shuoGG_re.ico'))
    mainWindow.show()
    sys.exit(app.exec_())
