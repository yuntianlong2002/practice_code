#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example shows a QtGui.QProgressBar widget.

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):  

        self.col = QtGui.QColor(0, 0, 0)      

        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150, 20, 800, 700)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())

        self.data=[0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,
        0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,
        0, 25, 50, 75, 100, 125, 150, 175, 200, 225,  
        50, 100, 0, 25, 200, 150, 25, 125, 0, 0]

        self.btn = QtGui.QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.changeColor)
        self.step = 0
        
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle('QtGui.QProgressBar')
        self.show()
        
    def changeColor(self):
      
        if self.step >= len(self.data):
        
            self.timer.stop()
            self.btn.setText('Finished')
            self.step = 0;
            return
            
        self.step = self.step + 1
        self.col.setRed(self.data[self.step])                
        self.col.setGreen(self.data[self.step])             
        self.col.setBlue(self.data[self.step])

        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())  

    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
            
        else:
            self.timer.start(100)
            self.btn.setText('Stop')
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    