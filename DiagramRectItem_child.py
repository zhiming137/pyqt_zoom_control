# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4 import QtGui
from DiagramRectItem import DiagramRectItem

class DiagramRectItem_child(DiagramRectItem):  
    def __init__(self, parent=None, scene=None): 
        super(DiagramRectItem_child, self).__init__(parent, scene)
        self.setBrush(QtGui.QColor(0, 255, 0))
        self.setPen(QtGui.QColor(255, 0, 0))
        self.setOpacity(0.25)
