from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
import sys
import core.crawling


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #ui.connect_event()

    MainWindow.show()
    sys.exit(app.exec_())


