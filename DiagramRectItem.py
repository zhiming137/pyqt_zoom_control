# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4 import QtGui

class ResizeFocusItem(QtGui.QGraphicsRectItem):  
    """
                    缩放锚点控制
    """
    def __init__(self, parent=None, type='', scene=None):  
        QtGui.QGraphicsRectItem.__init__(self, parent=parent.item, scene=scene)  
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)  
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable) 
        self.setFlag(QtGui.QGraphicsItem.ItemSendsGeometryChanges,  True) 
        self.setAcceptsHoverEvents(True) #开启hover事件
        
        self.parent = parent  #父类
        self.type   = type    #锚点类型
        self.basePos = self.pos() # 默认锚点位置
        
        # 各类型选中鼠标效果
        self.typeCursor = {
                        'lt' : QtCore.Qt.SizeFDiagCursor,
                        'tc' : QtCore.Qt.SizeVerCursor,
                        'rt' : QtCore.Qt.SizeBDiagCursor,
                        'lc' : QtCore.Qt.SizeHorCursor,
                        'rc' : QtCore.Qt.SizeHorCursor,
                        'lb' : QtCore.Qt.SizeBDiagCursor,
                        'bc' : QtCore.Qt.SizeVerCursor,
                        'rb' : QtCore.Qt.SizeFDiagCursor
                        }
        self.setBrush(QtGui.QColor(0, 0, 255))
        self.setPen(QtGui.QColor(255, 0, 0))
        self.setOpacity(1)
        self.setRect(0, 0, 5, 5) #锚点宽高
        newpos = self.getNewPos()
        self.setPos(newpos[0],newpos[1])
    
    def paint(self, painter, options, widget):  
        QtGui.QGraphicsRectItem.paint(self, painter, options, widget)  
    def getSelect(self):
        return self.isSelected()
    def hoverEnterEvent(self, event):
        """
                                鼠标经过时设置鼠标样式
        """
        if self.isVisible() == False:
            return
        super(ResizeFocusItem, self).hoverEnterEvent(event)
        self.setCursor(QtGui.QCursor(self.typeCursor[self.type]))
    
    
    def mouseMoveEvent(self, event):
        """
                                选中移动事件调整父类大小
        """
        if self.isVisible() == False:
            return
        super(ResizeFocusItem, self).mouseMoveEvent(event)
        away   = self.basePos-self.pos()
        ax = away.x()
        ay = away.y()
        
        prect = self.parent.item.rect()
        width = prect.width()
        height = prect.height()
        x = 0
        y = 0
        if self.type == 'lt':   #右下
            width  = width  + ax
            height = height +ay
            x = -ax
            y = -ay
            #self.parent.moveBy(-pos.x(), -pos.y())
            #self.parent.setPos(100, 100)
        elif self.type == 'tc':  #上中
            width  = width
            height = height + ay
            x = 0
            y = -ay
            #self.parent.moveBy(0, -pos.y())
        elif self.type == 'rt':  #左中
            width  = width - ax
            height = height + ay
            x = 0
            y = -ay
            #self.parent.moveBy(0, -pos.y())
        elif self.type == 'lc':  #左中
            width  = width + ax
            height = height
            x = -ax
            y = 0
            #self.parent.moveBy(-pos.x(),0)
        elif self.type == 'rc':  #右中
            width  = width - ax
            height = height
            #self.parent.moveBy(0,pos.y())
        elif self.type == 'lb':  #左下
            width  = width  + ax
            height = height - ay
            x = -ax
            y = 0
            #self.parent.moveBy(-pos.x(),0)
        elif self.type == 'bc': #下中
            width  = width
            height = height - ay
        elif self.type == 'rb': #右下
            width  = width - ax
            height = height - ay
            
        
        if(width < 30):
            width = 30
            x = 0
            
        if(height < 30):
            height = 30
            y = 0
        self.parent.item.setRect(0,0, width, height)
        self.parent.item.moveBy(x,y)
        
        self.basePos = self.pos()
        self.parent.updatePos() #更新锚点位置
        #self.parent.item.showPosTextObj.updatePos() #更新显示文字坐标
        
        #print "mouseMoveEvent"
    
    def mousePressEvent(self, event):
        self.basePos = self.pos()
        super(ResizeFocusItem, self).mousePressEvent(event)
        #print "mousePressEvent"
    def update(self):
        newpos = self.getNewPos()
        self.setPos(newpos[0],newpos[1])
        
    def getNewPos(self):
        prect = self.parent.item.rect()
        height = prect.height()
        width = prect.width()
        x = prect.x()
        y = prect.y()
        typePos = {
                        'lt' : ( x, y ),
                        'tc' : ( (width-5)/2, 0 ),
                        'rt' : ( width-5, y),
                        'lc' : ( x/2, (height-5)/2 ),
                        'rc' : ( width-5, (height-5)/2 ),
                        'lb' : ( x, (height-5) ),
                        'bc' : ( (width-5)/2, height-5 ),
                        'rb' : ( width-5, height-5 )
                        }
        return typePos[self.type]
        


class ResizeFocus():  
    """
                    缩放控制器
    """
    def __init__(self, parent=None, scene=None):  
        #lt      tc      rt
        #lc      cc      rc
        #lb      bc      rb
        self.item = parent
        self.focusObjList = {}
        
        type = ('lt','tc','rt','lc','rc','lb','bc','rb')
        for i in type:
            self.focusObjList[i] = ResizeFocusItem(self, type=i, scene=scene)
            #self.clist[i].setPos(100,100)
    def updatePos(self):
        for i in self.focusObjList:
            self.focusObjList[i].update()
    def setIsVisble(self, b):
        for i in self.focusObjList:
            self.focusObjList[i].setVisible(b)
    def getSelect(self):
        for i in self.focusObjList:
            if self.focusObjList[i].getSelect():
                return True
        return False
    
class DiagramRectItem(QtGui.QGraphicsRectItem):  
    def __init__(self, parent=None, scene=None):  
        QtGui.QGraphicsRectItem.__init__(self, parent=parent, scene=scene)  
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)  #使边框可选中
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)  #使边框可跟鼠标移动
        #self.setFlag(QtGui.QGraphicsItem.ItemClipsToShape)  #细边框
        self.setFlag(QtGui.QGraphicsItem.ItemSendsGeometryChanges,  True) 
        self.setFlag(QtGui.QGraphicsItem.ItemIgnoresParentOpacity, False)
        self.setAcceptsHoverEvents(True)
        self.setAcceptDrops(True)
        self.setSelected(True) #默认选中
        
        #self.setBrush(QtGui.QColor(0, 255, 0))
        #self.setPen(QtGui.QColor(255, 0, 0))
        #self.setOpacity(0.25)

        #大小控制器
        self.scene = scene
        #self.showPosPixObj = ShowItemPosPix(self, scene=self.scene)
        self.changed = ResizeFocus(self, scene=self.scene) #显示缩放锚点
        #self.showPosTextObj = ShowItemPosText(self, scene=self.scene) #显示坐标
        
        
        #self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor));
        
    def paint(self, painter, options, widget):  
        #print self.rect().height()
        #print self.pos()
        
        self.changed.updatePos() #更新锚点坐标
        #self.showPosPixObj.updatePos()
        if self.isSelected():  
            self.changed.setIsVisble(True)
        else:
            if self.changed.getSelect() == False:
                self.changed.setIsVisble(False)
        
        QtGui.QGraphicsRectItem.paint(self, painter, options, widget)

    def dragMoveEvent(self, event):
        print event
        super(DiagramRectItem, self).dragMoveEvent(event)
    def mouseMoveEvent(self, event):
        #print event
        super(DiagramRectItem, self).mouseMoveEvent(event)
        #print "item mouseMoveEvent"
        #self.showPosTextObj.updatePos() #更新显示文字坐标
        
        self.changed.updatePos() #更新锚点坐标
        #self.showPosPixObj.updatePos()
    def mousePressEvent(self, event):
        super(DiagramRectItem, self).mousePressEvent(event)
        #print "mousePressEvent"
    
    def mouseReleaseEvent(self, event):
        super(DiagramRectItem, self).mouseReleaseEvent(event)
        #print  "item mouseReleaseEvent"
        
        
    def hoverEnterEvent(self, event):
        super(DiagramRectItem, self).hoverEnterEvent(event)
        #print "item hoverEnterEvent"
        
        self.scene.skipLayerSelected = True
        
    def hoverLeaveEvent(self, event):
        super(DiagramRectItem, self).hoverLeaveEvent(event)
        #print "item hoverLeaveEvent"
        self.scene.skipLayerSelected = False
        
    def hoverMoveEvent(self, event):
        super(DiagramRectItem, self).hoverMoveEvent(event)
        #print "hoverMoveEvent"
        
    def dragEnterEvent(self, event):
        super(DiagramRectItem, self).dragEnterEvent(event)
        #print "dragEnterEvent"
        
    def dragLeaveEvent(self, event):
        super(DiagramRectItem, self).dragLeaveEvent(event)
        #print "dragLeaveEvent"
        
    def dragMoveEvent(self, event):
        super(DiagramRectItem, self).dragMoveEvent(event)
        print "dragMoveEvent"
        
    def focusInEvent(self, event):
        super(DiagramRectItem, self).focusInEvent(event)
        print "focusInEvent"
