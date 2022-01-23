from PyQt5 import QtCore, QtWidgets, QtGui
from os import environ

import errno, os, stat, shutil, main

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class myFileExplorer(main.Ui_MainWindow, QtWidgets.QMainWindow):
    
    list_path_back = list()
    list_path_forward = list()
    newname = ""
    selected_path = ""
    copy_cut_path =""
    signal = ""

    def __init__(self):
        super(myFileExplorer, self).__init__()
        self.setupUi(self)
        self.tree()
        self.list()
        self.event_button_setup()
     
    
    def tree(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.clicked.connect(self.tree_on_clicked)
        self.treeView.setSortingEnabled(True)
    
    def list(self):
        self.fileModel = QtWidgets.QFileSystemModel()
        self.fileModel.setRootPath((QtCore.QDir.rootPath()))
        self.listView.setModel(self.fileModel)
        self.listView.doubleClicked.connect(self.list_on_doubleclicked)
        self.listView.clicked.connect(self.save_path)
    
    def tree_on_clicked(self, index):
        currentpath = self.model.filePath(index)
        self.listView.setRootIndex(self.fileModel.setRootPath(currentpath))
        self.path.setText(currentpath)
        self.list_path_back.append(currentpath)
        self.list_path_forward.clear()
    

    def list_on_doubleclicked(self, index):
        currentpath = self.fileModel.filePath(index)
        self.listView.setRootIndex(self.fileModel.setRootPath(currentpath))
        self.path.setText(currentpath)
        self.list_path_back.append(currentpath)
        self.list_path_forward.clear()
        if not os.path.isdir(currentpath):
            os.startfile(currentpath)
        
    def save_path(self, index):
        self.selected_path = self.fileModel.filePath(index)
        
    def event_button_setup(self):
        self.Paste.clicked.connect(self.paste_clicked)
        self.Copy.clicked.connect(self.copy_clicked)
        self.Cut.clicked.connect(self.cut_clicked)
        self.Delete.clicked.connect(self.delete_clicked)
        self.Rename.clicked.connect(self.rename_clicked)
        self.Newfolder.clicked.connect(self.newfolder_clicked)
        self.upto.clicked.connect(self.upto_clicked)
        self.back.clicked.connect(self.back_clicked)
        self.forward.clicked.connect(self.forward_clicked)

    def paste_clicked(self):
        if self.signal == "copy" or self.signal == "cut":
            try:
                destination = self.path.text()
                if os.path.isdir(self.copy_cut_path):
                    os.makedirs(os.path.join(destination, os.path.basename(self.copy_cut_path)))  
                    destination = os.path.join(destination, os.path.basename(self.copy_cut_path))
                    for item in os.listdir(self.copy_cut_path):
                        s = os.path.join(self.copy_cut_path, item)
                        d = os.path.join(destination , item)
                        if os.path.isdir(s):
                            shutil.copytree(s, d)
                        else:
                            shutil.copy2(s, d)
                else:
                    shutil.copy2(self.copy_cut_path, destination)
                
                if self.signal == "cut":
                    def handleRemoveReadonly(func, path, exc):
                        excvalue = exc[1]
                        if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
                            os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
                            func(path)
                        else:
                            raise
                    try:
                        if os.path.isdir(self.copy_cut_path):
                            shutil.rmtree(self.copy_cut_path,ignore_errors=False, onerror=handleRemoveReadonly)
                        else:
                            os.remove(self.copy_cut_path)
                    except:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Warning)
                        msg.setText("Can't delete the old file!")
                        msg.setWindowTitle("Warning")
                        msg.setWindowIcon(QtGui.QIcon('image/warning.png'))
                        msg.exec_()
            except:
                if os.path.exists(os.path.join(destination, os.path.basename(self.copy_cut_path))):
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Your file/folder is exist. Please rename the old file/folder.")
                    msg.setWindowTitle("Warning")
                    msg.setWindowIcon(QtGui.QIcon('image/warning.png'))
                    msg.exec_()
                else: pass
                
        else: pass
        self.selected_path =""

    def copy_clicked(self):
        self.signal = "copy"
        self.copy_cut_path = self.selected_path
        self.selected_path = ""
        
    def cut_clicked(self):
        self.signal = "cut"
        self.copy_cut_path = self.selected_path
        self.selected_path = ""
    
    def delete_clicked(self):
        self.signal = "delete"

        def handleRemoveReadonly(func, path, exc):
            excvalue = exc[1]
            if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
                os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
                func(path)
            else:
                raise
        try:
            if os.path.isdir(self.selected_path):
                shutil.rmtree(self.selected_path,ignore_errors=False, onerror=handleRemoveReadonly)
            else:
                os.remove(self.selected_path)
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Can't delete file!")
            msg.setWindowTitle("Warning")
            msg.setWindowIcon(QtGui.QIcon('image/warning.png'))
            msg.exec_()
    
    def rename_clicked(self):
        try:
            self.signal = "rename"
            self.rname = QtWidgets.QLineEdit(self.frame)
            self.rname.setObjectName("rname")
            self.horizontalLayout_2.addWidget(self.rname)

            self.done = QtWidgets.QPushButton(self.frame)
            self.done.setObjectName("done")
            self.horizontalLayout_2.addWidget(self.done)
            _translate = QtCore.QCoreApplication.translate
            self.done.setText(_translate("MainWindow", "Done"))

            self.done.clicked.connect(self.done_clicked)
        except: pass

    def done_clicked(self):
        try:
            self.newname = self.rname.text()
            self.rname.deleteLater()
            self.done.deleteLater()
            extension = os.path.splitext(self.selected_path)[1]
            newName = os.path.join(os.path.dirname(self.selected_path),self.newname+extension)
            os.rename(self.selected_path, newName)
            
        except:
            newName = os.path.join(os.path.dirname(self.selected_path),self.newname+extension) 
            if os.path.exists(newName):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You enter an exist filename! Try again")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QtGui.QIcon('image/warning.png'))
                msg.exec_()
            else: pass
        self.selected_path = ""
    
    def newfolder_clicked(self):
        try:
            currentpath = self.path.text()
            newpath = os.path.join(currentpath, "New folder")
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            else:
                i = 0
                while True:
                    newpath1 = newpath +" ("+ str(i) + ")"
                    if not os.path.exists(newpath1):
                        os.makedirs(newpath1)
                        break
                    else:
                        i = i + 1
        except:
            pass

    def upto_clicked(self):
        try: 
            uptopath = os.path.dirname(self.path.text()) 
            self.listView.setRootIndex(self.fileModel.setRootPath(uptopath))
            self.path.setText(uptopath)
            self.list_path_back.append(self.path.text())
            self.list_path_forward.clear()
        except:
            pass
    
    def back_clicked(self):
        try:
            backpath = self.list_path_back[-2]
            self.listView.setRootIndex(self.fileModel.setRootPath(backpath))
            self.path.setText(backpath)
            self.list_path_forward.append(self.list_path_back[-1])
            self.list_path_back.pop(-1)
        except:
            pass

    def forward_clicked(self):
        try:
            forwardpath = self.list_path_forward[-1]
            self.listView.setRootIndex(self.fileModel.setRootPath(forwardpath))
            self.path.setText(forwardpath)
            self.list_path_back.append(self.path.text())
            self.list_path_forward.pop(-1)
        except:
            pass

if __name__ == '__main__':
    suppress_qt_warnings()
    app = QtWidgets.QApplication([])
    fe = myFileExplorer()
    fe.show()
    app.exec_()
    
    
