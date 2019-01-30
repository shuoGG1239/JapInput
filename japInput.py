import ui_japInput
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QSize

WHITE = "#FFFFFF"
BLACK = "#000000"
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"
PURPLE = "#B23AEE"
WATCHET = "#1C86EE"
LIGHTGREEN = "#ECFEFE"
BLUEGREEN = "#33CCCC"
DEEPBLUEGREEN = "#015F5F"
DARKBLUEGREEN = "#28AAAA"
GRAY = "#999999"
LIGHTGRAY = "#CCCCCC"



class JapInput(QWidget):

    def __init__(self):
        super(JapInput, self).__init__()
        self.ui = ui_japInput.Ui_widget()
        self.ui.setupUi(self)
        self.init_style()
        self.m_move = False

    def lineEditQss(self, normalColor, focusColor):
        str1 = "QLineEdit{border-style:none;padding:4px;border-radius:20px;border:3px solid %s;selection-color:%s;selection-background-color:%s;}" % (
            normalColor, WHITE, focusColor)
        str2 = "QLineEdit:focus{border:3px solid %s;}" % (focusColor)
        str3 = "QLineEdit:disabled{color:%s;}" % (LIGHTGRAY)
        return str1 + str2 + str3

    def listViewQss(self):
        str1 = "QListWidget{border-radius:20px;border:8px solid #33CCCC;}"
        str2 = "QListWidget::Item{border-radius:5px;}"
        return str1+str2

    def init_style(self):
        s = '#widget{background: transparent;}'
        self.setStyleSheet(s)
        self.ui.lineEdit.setStyleSheet(self.lineEditQss(GRAY, BLUEGREEN))


    @pyqtSlot()
    def on_btnMin_clicked(self):
        print('min')
        newItem = QListWidgetItem()
        newItem.setSizeHint(QSize(100,50))
        newItem.setText("123")
        self.ui.listWidget.addItem(newItem)

    @pyqtSlot()
    def on_btnClose_clicked(self):
        self.close()

    @pyqtSlot(QListWidgetItem)
    def on_listWidget_rowsInserted(self, item):
        print(444)
        self.ui.listWidget.resize(self.width(), self.height() + item.height())

    @pyqtSlot(QListWidgetItem)
    def on_listWidget_itemClicked(self, item):
        print(123)


    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_move = True
            self.m_startPoint = e.globalPos()
            self.m_windowPoint = self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            r_pos = e.globalPos() - self.m_startPoint
            self.move(self.m_windowPoint + r_pos)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_move = False
