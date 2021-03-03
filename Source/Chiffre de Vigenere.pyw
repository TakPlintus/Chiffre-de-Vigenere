from PyQt5 import QtWidgets, QtGui

from UI_file import Ui_MainWindow
import sys

eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)

    def start(self):
        key = self.ui.lineEdit.text()
        if not key.isalpha():
            key = ''.join(filter(str.isalpha, key))
            self.ui.lineEdit.setText(key)
        text = self.ui.lineEdit_2.text().split()

        if len(''.join(text)) > len(key):
            j = 0
            while len(key) + 1 <= len(''.join(text)):
                key += key[j]
                j += 1

        text2 = ''
        if self.ui.comboBox.currentText() == 'EN':
            x = 0
            for i in range(len(text)):
                t = text[i]
                key = key[x:]
                for j in range(len(t)):
                    if t[j].lower() in eng_alphabet:
                        x = j + 1
                        p, k = eng_alphabet.find((t[j]).lower()), eng_alphabet.find((key[j]).lower())
                        if self.ui.checkBox.isChecked():
                            text2 += eng_alphabet[(p - k + 26) % 26].upper() if t[j].isupper() else eng_alphabet[
                                (p - k + 26) % 26]
                        else:
                            text2 += eng_alphabet[(p + k) % 26].upper() if t[j].isupper() else eng_alphabet[
                                (p + k) % 26]
                    elif not t[j].lower().isalpha():
                        text2 += t[j]
                    else:
                        QtWidgets.QMessageBox.critical(self, "NOOOOOOOOO", "Wrong language selected!")
                        break
                text2 += ' '
            self.ui.textEdit.setPlainText(text2)
        elif self.ui.comboBox.currentText() == 'RU':
            x = 0
            for i in range(len(text)):
                t = text[i]
                key = key[x:]
                for j in range(len(t)):
                    if t[j].lower() in rus_alphabet:
                        x = j + 1
                        p, k = rus_alphabet.find((t[j]).lower()), rus_alphabet.find((key[j]).lower())
                        if self.ui.checkBox.isChecked():
                            text2 += rus_alphabet[(p - k + 32) % 32].upper() if t[j].isupper() else rus_alphabet[
                                (p - k + 32) % 32]
                        else:
                            text2 += rus_alphabet[(p + k) % 32].upper() if t[j].isupper() else rus_alphabet[
                                (p + k) % 32]
                    elif not t[j].lower().isalpha():
                        text2 += t[j]
                    else:
                        QtWidgets.QMessageBox.critical(self, "NOOOOOOOOO", "Wrong language selected!")
                        break
                text2 += ' '
            self.ui.textEdit.setPlainText(text2)


app = QtWidgets.QApplication([])
app.setWindowIcon(QtGui.QIcon('Data/logo.png'))
application = window()
application.setFixedSize(800, 600)
application.show()

sys.exit(app.exec())
