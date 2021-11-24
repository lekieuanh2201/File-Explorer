# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QtGui.QIcon('image/icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Tool = QtWidgets.QGroupBox(self.frame)
        self.Tool.setObjectName("Tool")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Tool)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
       
        self.Copy = QtWidgets.QPushButton(self.Tool)
        self.Copy.setIcon(QtGui.QIcon('image/copy.png'))
        self.Copy.setObjectName("Copy")
        self.horizontalLayout_2.addWidget(self.Copy)
       
        self.Cut = QtWidgets.QPushButton(self.Tool)
        self.Cut.setIcon(QtGui.QIcon('image/cut.png'))
        self.Cut.setObjectName("Cut")
        self.horizontalLayout_2.addWidget(self.Cut)
       
        self.Paste = QtWidgets.QPushButton(self.Tool)
        self.Paste.setIcon(QtGui.QIcon('image/paste.png'))
        self.Paste.setObjectName("Paste")
        self.horizontalLayout_2.addWidget(self.Paste)
       
        self.Delete = QtWidgets.QPushButton(self.Tool)
        self.Delete.setIcon(QtGui.QIcon('image/delete.png'))
        self.Delete.setObjectName("Delete")
        self.horizontalLayout_2.addWidget(self.Delete)
       
        self.Newfolder = QtWidgets.QPushButton(self.Tool)
        self.Newfolder.setIcon(QtGui.QIcon('image/new folder.png'))
        self.Newfolder.setObjectName("Newfolder")
        self.horizontalLayout_2.addWidget(self.Newfolder)
       
        self.Rename = QtWidgets.QPushButton(self.Tool)
        self.Rename.setIcon(QtGui.QIcon('image/rename.png'))
        self.Rename.setObjectName("Rename")
        self.horizontalLayout_2.addWidget(self.Rename)
        
        self.gridLayout_2.addWidget(self.Tool, 0, 0, 1, 6)
        
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setText("")
        self.back.setIcon(QtGui.QIcon('image/undo.png'))
        self.back.setObjectName("back")
        self.gridLayout_2.addWidget(self.back, 1, 0, 1, 1)
        
        self.forward = QtWidgets.QPushButton(self.frame)
        self.forward.setText("")
        self.forward.setIcon(QtGui.QIcon('image/redo.png'))
        self.forward.setObjectName("forward")
        self.gridLayout_2.addWidget(self.forward, 1, 1, 1, 1)
        
        self.upto = QtWidgets.QPushButton(self.frame)
        self.upto.setText("")
        self.upto.setIcon(QtGui.QIcon('image/upto.png'))
        self.upto.setObjectName("upto")
        self.gridLayout_2.addWidget(self.upto, 1, 2, 1, 1)
        
        self.Path = QtWidgets.QLabel(self.frame)
        self.Path.setObjectName("Path")
        self.gridLayout_2.addWidget(self.Path, 1, 3, 1, 1)
        
        self.path = QtWidgets.QLineEdit(self.frame)
        self.path.setObjectName("path")
        self.gridLayout_2.addWidget(self.path, 1, 4, 1, 2)
        
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.treeView.setObjectName("treeView")
        self.gridLayout_2.addWidget(self.treeView, 2, 0, 1, 5)
        
        self.listView = QtWidgets.QListView(self.frame)
        self.listView.setObjectName("listView")
        self.gridLayout_2.addWidget(self.listView, 2, 5, 1, 1)
        
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Explorer_KA"))
        self.Tool.setTitle(_translate("MainWindow", "Tool"))
        self.Copy.setText(_translate("MainWindow", "Copy"))
        self.Cut.setText(_translate("MainWindow", "Cut"))
        self.Paste.setText(_translate("MainWindow", "Paste"))
        self.Delete.setText(_translate("MainWindow", "Delete"))
        self.Newfolder.setText(_translate("MainWindow", "New folder"))
        self.Rename.setText(_translate("MainWindow", "Rename"))
        self.Path.setText(_translate("MainWindow", "Path"))


if __name__ == "__main__":
    import sys
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
