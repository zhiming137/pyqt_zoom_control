# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\eric4pro\demo4\MainWindow.ui'
#
# Created: Thu Mar 21 17:03:02 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.editView = QtGui.QGraphicsView(self.centralWidget)
        self.editView.setGeometry(QtCore.QRect(10, 20, 471, 551))
        self.editView.setObjectName(_fromUtf8("editView"))
        self.treeView = QtGui.QTreeView(self.centralWidget)
        self.treeView.setGeometry(QtCore.QRect(550, 20, 241, 192))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.tableView = QtGui.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(530, 290, 256, 192))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

