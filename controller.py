from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_submit.clicked.connect(lambda: self.submit())

    def submit(self):
        cookie = self.cookie.value() * 1.50
        turkey_sandwich = self.turkey_sandwich.value() * 4.50
        ham_sandwich = self.ham_sandwich.value() * 5.50
        water = self.water.value()
        pop = self.pop.value() * 2
        total = cookie + turkey_sandwich + ham_sandwich + water + pop
        self.amount_due.setText(f'Final Amount Due: ${total:.2f}')

    