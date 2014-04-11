# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from DiagramScene import *
from DiagramRectItem import *


from Ui_MainWindow import Ui_MainWindow
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

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.scene = DiagramScene(self.editView)
        self.scene.setSceneRect(QtCore.QRectF(0, 0, 500, 500))
        
        self.scene.itemSelected.connect(self.itemSelected)
         
        self.editView.setRenderHint(QtGui.QPainter.Antialiasing)  
        self.editView.setScene(self.scene)
    
    def itemSelected(self, item):
        self.initTreeView(item)
    
    def initTreeView(self, it):
        treeModel = QStandardItemModel()
        treeModel.setColumnCount(2)
        treeModel.setHeaderData(0,Qt.Horizontal,"Property", 0)
        treeModel.setHeaderData(1,Qt.Horizontal,'Value', 0)
        parentItem = treeModel.invisibleRootItem()
        '''
        item = QStandardItem('geometry')
        item.setBackground(QBrush(QtGui.QColor(128, 128, 128)))
        item.setEditable(False)
        
        for j in ('x', 'y', 'width', 'height'):
                item1 = QStandardItem(j)
                item1.setBackground(QBrush(QtGui.QColor(255, 255, 0)))
                item1.setEditable(False)
                item.appendRow(item1)
                print item.row(), item1.row()
        
        con = []
        for i in (str(it.y()),str(it.x()), str(it.rect().width()), str(it.rect().height())):
            item1 = QStandardItem(i)
            item1.setBackground(QBrush(QtGui.QColor(255, 255, 0)))
            con.append(item1)
        item.appendColumn(con)
        
        parentItem.appendRow(item)
        '''
        item = QStandardItem('geometry')
        item.setBackground(QBrush(QtGui.QColor(128, 128, 128)))
        item.setEditable(False)
        #parentItem.appendRow(item)
        item1 = QStandardItem('geometry')
        for i in range(8):
            treeModel.setItem(i, 0, QStandardItem('geometry'))
            treeModel.setItem(i, 1, QStandardItem('value'))
        
        #self.treeView.setAllColumnsShowFocus(True)
        self.treeView.setModel(treeModel)
        self.tableView.setModel(treeModel)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
