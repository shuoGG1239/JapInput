import ui_japInput
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QSize
import jap_dict as jd


class JapInput(QWidget):

    def __init__(self):
        super(JapInput, self).__init__()
        self.ui = ui_japInput.Ui_widget()
        self.ui.setupUi(self)
        self.init_style()
        self.init_ui_stat()
        self.init_data()

    def init_data(self):
        jd.init_dict()
        self.index = 0

    def init_style(self):
        with open('style.qss', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def init_ui_stat(self):
        self.m_move = False
        self.ui.listWidget.clear()

    @pyqtSlot()
    def on_btnMin_clicked(self):
        print('min')
        if self.ui.listWidget.count() < 4:
            item = self.ui.listWidget.newItem('10086')
            self.ui.listWidget.addItem(item)

    @pyqtSlot()
    def on_btnClose_clicked(self):
        self.close()

    @pyqtSlot(QListWidgetItem)
    def on_listWidget_sgnAddItem(self, item):
        self.ui.listWidget.show()
        self.ui.listWidget.resize(self.ui.listWidget.width(),
                                  self.ui.listWidget.height() + item.sizeHint().height() + 2)

    @pyqtSlot()
    def on_listWidget_sgnClearItem(self):
        self.ui.listWidget.hide()
        self.ui.listWidget.resize(self.ui.listWidget.width(), 0)

    @pyqtSlot(QListWidgetItem)
    def on_listWidget_itemClicked(self, item):
        print(123)

    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        raw_text = text[self.index:]
        if raw_text in jd.jp_dict:
            if self.index == 0:
                self.ui.lineEdit.setText(jd.jp_dict[raw_text])
            else:
                self.ui.lineEdit.setText(text[:self.index] + jd.jp_dict[raw_text])
            self.index += 1

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
