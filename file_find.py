import sys, os, platform, subprocess
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(400, 250, 600, 300)
        self.setWindowTitle("Game Tutorial")
        #self.setWindowIcon(QtGui.QIcon('ball.png'))

        global file_list[]
        
        #Actions for Main Menu
        mainReturn = QtGui.QAction("&Main Menu", self)
        mainReturn.setShortcut("Ctrl+R")
        mainReturn.setStatusTip('Return to Main Menu')
        mainReturn.triggered.connect(Window)
        
        exitAction = QtGui.QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip('Close Interface')
        exitAction.triggered.connect(self.close_interface)

      
        #Create Main Menu
        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(mainReturn)
        fileMenu.addAction(exitAction)
        self.home()

    def home(self):
        
        self.create_folder_option()
        self.show()

    def create_folder_option(self):
        x = 455
        y = 57

        bv1 = QtGui.QPushButton("open folder", self)
        bv1.clicked.connect(self.open_folder)
        bv1.resize(bv1.minimumSizeHint())
        bv1.move(x, y)
        y += 70
            
    def open_folder(self):
        
        dir_ = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        self.list_files(dir_)

    def list_files(self, dir_):
        print (dir_)
        for file in os.listdir(dir_):
            print (file)
        
    def close_interface(self):
        choice = QtGui.QMessageBox.question(self, 'Exit', "Are you sure?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
        
if __name__ == "__main__":        
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
        
