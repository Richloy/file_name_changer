import sys, os
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        
        self.name = ""
        self.season = ""
        self.setGeometry(400, 250, 600, 300)
        self.setWindowTitle("Game Tutorial")

        #Select Folder for files   
        self.file_list = []
        self.dir_ = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        
        for file in os.listdir(self.dir_):
            if file.endswith('.txt') or file.endswith('.mp4'):
                self.file_list.append(file)
                
        #Select file with new names
        f = open('rename.txt', 'r')
        
        rename_list = []
        lines = f.readlines()
        for line in lines:
            line_tokens = line.split('\t')
            rename_list.append(line_tokens[1])
        f.close()
        
        for i in range(len(rename_list)):
            print(rename_list[i])

        #Create some functionality to GUI
        self.label_series = QtGui.QLabel("Not Selected", self)
        self.label_series.move(300, 10)
        self.label_season = QtGui.QLabel("Not Selected", self)
        self.label_season.move(300, 45)
        self.btn = QtGui.QPushButton("Select Series", self)
        self.btn.move(400, 10)
        self.btn.clicked.connect(self.get_text)
        self.btn = QtGui.QPushButton("Select Season", self)
        self.btn.move(400, 45)
        self.btn.clicked.connect(self.get_season)
        self.btn_convert = QtGui.QPushButton("Select Text", self)
        self.btn_convert.move(400, 100)
        self.btn_convert.clicked.connect(self.convert_files)
        
        self.home()
        
    def convert_files(self):

        print(self.name)
        print(self.season)
        
    def home(self):
        
        #self.print_name()
        x = 25
        y = 10
        for i in range(len(self.file_list)):
            label = QtGui.QLabel(self.file_list[i], self)
            label.move(x, y)
            y += 15
            print(self.file_list[i])
        
        self.show()

    def get_text(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Text Input Dialog', 'Enter The Series:')
	
        if ok:
            self.label_series.setText(str(text))
            self.name = str(text)

    def get_season(self):

        text, ok = QtGui.QInputDialog.getText(self, 'Text Input Dialog', 'Enter The Season:')
	
        if ok:
            if len(text) < 2:
                text = "S0" + str(text)
                self.label_season.setText(text)
            else:
                text = "S" + str(text)
                self.label_season.setText(text)
            self.season = text
        
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
        
