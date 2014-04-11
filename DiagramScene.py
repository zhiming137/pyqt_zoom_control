# -*- coding: utf-8 -*-
import math
from PyQt4 import QtCore
from PyQt4.QtCore import *
from DiagramRectItem import *
from DiagramRectItem_child import *
from MainWindow import *

class DiagramScene(QtGui.QGraphicsScene):
    itemSelected = QtCore.pyqtSignal(QtGui.QGraphicsItem)
    def __init__(self, parent=None):
        super(DiagramScene, self).__init__(parent)
        #self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(0, 0, 255, 127)))
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QPixmap('images/background3.png')))
        
        self.press = False 
        self.pressPos   = QtCore.QPointF(0,0)  #默认按下位置
        self.releasePos = QtCore.QPointF(0,0)  #默认抬起位置
        self.selected = None #默认选区
        
        
        self.skipLayerList = []
        self.skipLayerSelected = False   #是否选中层
        
    def mousePressEvent(self, event):
        super(DiagramScene, self).mousePressEvent(event)
        
        self.press = True
        self.pressPos = event.scenePos()

    
    def mouseReleaseEvent(self, event):
        super(DiagramScene, self).mouseReleaseEvent(event)

        self.press = False
        self.releasePos = event.scenePos()
        self.releaseSelected() #删除选区
        if len(self.skipLayerList)>0:
            for item in self.skipLayerList:
                if item.isSelected():
                    self.itemSelected.emit(item)
                    break
    def mouseMoveEvent(self, event):
        super(DiagramScene, self).mouseMoveEvent(event)
        #print "scene mouseMoveEvent"
        if not self.skipLayerSelected:
            self.insertSelected(event)  #插入新选区
     
    def hoverEnterEvent(self, event):  
          pass
      
    def insertSelected(self, event):
        """
                                插入临时选区
        """
        if self.press:
            movePos = event.scenePos()  #移动的坐标
            pos = movePos - self.pressPos #坐标差
            x = self.pressPos.x()
            y = self.pressPos.y()
            width = pos.x()  #选框宽度
            height = pos.y() #选框高度
            #width = 30  #选框宽度
            #height = 30 #选框高度
            #print width,height
            if width<0 and height<0:
                x = movePos.x()
                y = movePos.y()
            elif width<0 and height>0:
                x += width
            elif width>0 and height<0:
                y += height
            
            width = math.fabs(width)
            height = math.fabs(height)
            
            if self.selected == None:
                self.selected = QtGui.QGraphicsRectItem(scene=self)
            self.selected.setRect(0,0,width,height)
            self.selected.setPos(x, y)
    def releaseSelected(self):
        if self.selected != None:
            rect = self.selected.rect();
            pos = self.selected.pos();
            self.addSkipLayer(rect,pos)
            
            self.removeItem(self.selected) #销毁选框
            self.selected = None  
    
    def addSkipLayer(self, rect, pos):
        skipLayer = DiagramRectItem(scene=self)
        #skipLayer = DiagramRectItem_child(scene=self)
        width  = rect.width()
        height = rect.height()
        if width<30:
            width = 30
        if height<30:
            height = 30
        skipLayer.setRect(0,0,width, height)
        skipLayer.setPos(pos.x(), pos.y())
        #skipLayer.showPosTextObj.updatePos()
        self.skipLayerList.append(skipLayer)
      
