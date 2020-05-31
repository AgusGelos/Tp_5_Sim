from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt

from el_Completo import generar_miles
import pandas as pd


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1879, 929)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 371, 111))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.txtDesde = QtWidgets.QLineEdit(self.groupBox)
        self.txtDesde.setGeometry(QtCore.QRect(140, 50, 113, 20))
        self.txtDesde.setObjectName("txtDesde")

        self.txtCantDias = QtWidgets.QLineEdit(self.groupBox)
        self.txtCantDias.setGeometry(QtCore.QRect(140, 20, 113, 20))
        self.txtCantDias.setObjectName("txtCantDias")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.btnIniciar = QtWidgets.QPushButton(self.groupBox)
        self.btnIniciar.setGeometry(QtCore.QRect(290, 80, 75, 23))
        self.btnIniciar.setObjectName("btnIniciar")
        self.btnIniciar.clicked.connect(self.on_click)

        self.txtHasta = QtWidgets.QLineEdit(self.groupBox)
        self.txtHasta.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.txtHasta.setObjectName("txtHasta")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.tabla = QtWidgets.QTableView(self.centralwidget)
        self.tabla.setGeometry(QtCore.QRect(10, 120, 1851, 781))
        self.tabla.setObjectName("tabla")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulación"))
        self.label_2.setText(_translate("MainWindow", "Día desde"))
        self.label.setText(_translate("MainWindow", "Cantidad de días"))
        self.btnIniciar.setText(_translate("MainWindow", "Iniciar"))
        self.label_3.setText(_translate("MainWindow", "Día hasta"))


    def on_click(self):
        df = generar_miles(int(self.txtCantDias.text()), int(self.txtDesde.text()), int(self.txtHasta.text()))
        self.tabla.setModel(pandasModel(df))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
