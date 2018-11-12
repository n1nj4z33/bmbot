import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QCoreApplication, QThread, pyqtSignal, QSettings

from mainwindow import Ui_MainWindow

import time

from market_maker import bitmex



class Thread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, app):
        QThread.__init__(self)
        self.app = app

    def run(self):
        bm = bitmex.BitMEX(base_url=self.app.lineEdit.text(),
                           apiKey=self.app.lineEdit_2.text(),
                           apiSecret=self.app.lineEdit_3.text(),
                           symbol=self.app.lineEdit_4.text(),
                           orderIDPrefix='')
        self.signal.emit('Жду открытия позиции...')
        while True:
            position = bm.position(self.app.lineEdit_4.text())
            if position['isOpen']:
                quantity = position['currentQty']
                self.signal.emit('Позиция отрылась по цене {}'.format(position['avgEntryPrice']))
                for order in bm.open_orders():
                    self.signal.emit('Отменяю ордер {}'.format(order['orderID']))
                    bm.cancel(order['orderID'])
                if quantity > 0:
                    price = position['avgEntryPrice'] + int(self.app.lineEdit_5.text())
                    self.signal.emit('Продаю по цене {}'.format(price))
                    bm.sell(quantity, price)
                    return
                elif quantity < 0:
                    price = position['avgEntryPrice'] - int(self.app.lineEdit_5.text())
                    self.signal.emit('Покупаю по цене {}'.format(price))
                    bm.buy(-quantity, price)
                    return
            time.sleep(5)


class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/icon.ico'))

        self.pushButton.clicked.connect(self.started)
        self._worker = Thread(self)
        self._worker.signal.connect(self._logging)
        self._worker.finished.connect(self.finished)

        self.settings = QSettings()
        base_url = self.settings.value('base_url', self.lineEdit.text(), type=str)
        api_key = self.settings.value('api_key', self.lineEdit_2.text(), type=str)
        api_secret = self.settings.value('api_secret', self.lineEdit_3.text(), type=str)
        symbol = self.settings.value('symbol', self.lineEdit_4.text(), type=str)
        n = self.settings.value('n', self.lineEdit_5.text(), type=str)

        self.lineEdit.setText(base_url)
        self.lineEdit_2.setText(api_key)
        self.lineEdit_3.setText(api_secret)
        self.lineEdit_4.setText(symbol)
        self.lineEdit_5.setText(n)

    def _logging(self, txt):
        self.textEdit.append(txt)

    def started(self):
        self._logging('Начал работу')
        self.pushButton.setEnabled(False)
        self._worker.start()

        self.settings.setValue('base_url', self.lineEdit.text())
        self.settings.setValue('api_key', self.lineEdit_2.text())
        self.settings.setValue('api_secret', self.lineEdit_3.text())
        self.settings.setValue('symbol', self.lineEdit_4.text())
        self.settings.setValue('n', self.lineEdit_5.text())
        self.settings.sync()

    def finished(self):
        self._logging('Закончил работу')
        self.pushButton.setEnabled(True)
        self._worker.quit()

def main():

    QCoreApplication.setApplicationName('Bmbot App')
    QCoreApplication.setOrganizationDomain('bmbot.com')
    QCoreApplication.setApplicationName('Bmbot')

    app = QtWidgets.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
