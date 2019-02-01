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
        self.jStat = 'hira'  # 'hira' 'kake'
        self.firstMove = True

    def init_style(self):
        with open('style.qss', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def init_ui_stat(self):
        self.m_move = False
        self.ui.listWidget.clear()

    @pyqtSlot()
    def on_btnMin_clicked(self):
        self.showMinimized()

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
        self.ui.lineEdit.setText(item.text())
        self.ui.listWidget.clear()
        self.ui.lineEdit.setFocus(True)

    @pyqtSlot(QListWidgetItem)
    def on_listWidget_sgnEnterItem(self, item):
        self.ui.lineEdit.setText(item.text())
        self.ui.listWidget.clear()
        self.ui.lineEdit.setFocus(True)

    @pyqtSlot()
    def on_listWidget_sgnTopupItem(self):
        self.ui.lineEdit.setFocus(True)
        self.ui.listWidget.item(0).setSelected(False)

    @pyqtSlot(str)
    def on_lineEdit_textEdited(self, text):
        index = 0
        for ch, i in zip(text, range(len(text))):
            if not jd.isJP_word(ch):
                index = i
                break
        raw_text = text[index:]
        if raw_text in jd.jp_dict:
            if index == 0:
                self.ui.lineEdit.setText(jd.jp_dict[raw_text])
            else:
                self.ui.lineEdit.setText(text[:index] + jd.jp_dict[raw_text])
        self.ui.listWidget.clear()
        self.ui.listWidget.addTextItems(self.getHints(text))

    @pyqtSlot()
    def on_lineEdit_sgnDownPress(self):
        self.ui.listWidget.setFocus(True)
        self.ui.listWidget.setCurrentRow(0)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_move = True
            self.m_startPoint = e.globalPos()
            self.m_windowPoint = self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            if self.firstMove:
                self.m_move = True
                self.m_startPoint = e.globalPos()
                self.m_windowPoint = self.frameGeometry().topLeft()
                self.firstMove = False
            r_pos = e.globalPos() - self.m_startPoint
            self.move(self.m_windowPoint + r_pos)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_move = False
            self.firstMove = True
            self.ui.lineEdit.setFocus(True)

    def switchType(self, jStat):
        """
        lineEdit切换为平假模式or片假模式
        @param jStat: hira kake
        """
        if jStat == self.jStat:
            return
        curText = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(self.doTransferJStat(curText, jStat))

    def getHints(self, rawText):
        hint1 = self.doTransfer(rawText, 'hira')
        hint2 = self.doTransferJStat(hint1, 'kake')
        if hint1 == '' and hint2 == '':
            return []
        return [hint2, hint1]

    def doTransfer(self, text, jStat):
        index = 0
        for ch, i in zip(text, range(len(text))):
            index = i
            if not jd.isJP_word(ch):
                break
            index += 1
        raw_text = text[index:]
        ret = str()
        if raw_text in jd.jp_dict:
            ret = jd.jp_dict[raw_text]
        if index > 0:
            ret = text[:index] + ret
        if jStat == 'kake':
            ret = self.doTransferJStat(ret, jStat)
        return ret

    def doTransferJStat(self, text, jStat):
        newText = str()
        if jStat == 'hira':
            for c in text:
                if c in jd.kake_hira_dict:
                    newText += jd.kake_hira_dict[c]
                else:
                    newText += c
        if jStat == 'kake':
            for c in text:
                if c in jd.hira_kake_dict:
                    newText += jd.hira_kake_dict[c]
                else:
                    newText += c
        return newText
