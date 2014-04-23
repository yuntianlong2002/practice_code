#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):  
        self.col = QtGui.QColor(0, 0, 0) #2 3 6 9 0 5 2

        self.data=[]
        self.compare = [0, 75, 113, 148, 175, 195, 212, 227, 242, 255]

        self.emptytick=5
        self.ifloop = 0
        self.serect_str=''  
        self.serect=[] 
        self.empty_seq=[]  

        self.square = QtGui.QFrame(self)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())

        self.btn = QtGui.QPushButton('Start', self)
        self.btn.clicked.connect(self.doAction)

        self.cb2 = QtGui.QCheckBox('Loop', self)
        self.cb2.stateChanged.connect(self.doChange)
        self.lbl4 = QtGui.QLabel()
        self.lbl4.setText('Peroid:')
        self.qle4 = QtGui.QLineEdit(self)
        self.qle4.setFixedWidth(50)
        self.qle4.setText('1000')


        self.lbl2 = QtGui.QLabel()
        self.lbl2.setText('Sequence:')
        self.qle2 = QtGui.QLineEdit(self)

        self.btn2 = QtGui.QPushButton('Create', self)
        self.btn2.clicked.connect(self.createSeq)

        self.lbl5 = QtGui.QLabel()
        self.lbl5.setText('Idle:')
        self.lcd = QtGui.QLCDNumber(self)
        self.sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sld.valueChanged.connect(self.lcd.display)

        sublayout1 = QtGui.QHBoxLayout()
        sublayout1.addWidget(self.lbl2)
        sublayout1.addWidget(self.qle2)
        sublayout1.addWidget(self.btn2)

        sublayout2 = QtGui.QHBoxLayout()
        sublayout2.addWidget(self.lbl5)
        sublayout2.addWidget(self.lcd)
        sublayout2.addWidget(self.sld)

        sublayout3 = QtGui.QHBoxLayout()
        sublayout3.addWidget(self.lbl4)
        sublayout3.addWidget(self.qle4)
        sublayout3.addWidget(self.cb2)
        sublayout3.setAlignment(QtCore.Qt.AlignHCenter)
        sublayout3.addStretch(9);

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.square)
        layout.addWidget(self.btn)
        layout.addLayout(sublayout3)
        layout.addLayout(sublayout1)
        layout.addLayout(sublayout2)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.changeColor)
        self.step = 0
        
        self.setLayout(layout)
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('QtGui.QProgressBar')
        self.show()
        
    def changeColor(self):
      
        if self.step >= len(self.data):
            
            if self.ifloop == 0:
                self.timer.stop()
                self.btn.setText('Start')

            self.step = 0;

            return
            
        
        self.col.setRed(self.data[self.step])                
        self.col.setGreen(self.data[self.step])             
        self.col.setBlue(self.data[self.step])

        self.step = self.step + 1
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())  

    def doChange(self, state):
        if state == QtCore.Qt.Checked:
            self.ifloop = 1
        else:
            self.ifloop = 0

    def createSeq(self):
        self.emptytick=self.lcd.intValue()
        self.empty_seq=[] 
        for x in range(0, self.emptytick):
            self.empty_seq=self.empty_seq+[0]

        self.serect_str=self.qle2.text()
        self.serect=self.serect_str.split(' ')
        self.serect=map(int,self.serect)

        for x in range(0,len(self.serect)):
            self.serect[x]=self.compare[self.serect[x]]

        self.data=self.empty_seq+self.compare+self.serect

        print(self.data)

    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
            
        else:
            time=int(self.qle4.text())
            self.timer.start(time)
            self.btn.setText('Stop')
            self.step=0;
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    