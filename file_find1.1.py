import sys, os
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        
        self.name = ""
        self.season = ""
        self.format = ""
        self.setGeometry(400, 250, 600, 300)
        self.setWindowTitle("File Name Changer")
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        #Select Folder for files   
        self.file_list = []
        self.dir_ = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        
        for file in os.listdir(self.dir_):
            if file.endswith(self.format):
                self.file_list.append(file)
                
        #Select file with new names
        f = open('rename.txt', 'r')
        
        self.rename_list = []
        lines = f.readlines()
        for line in lines:
            line_tokens = line.split('\t')
            self.rename_list.append(line_tokens[1])
        f.close()
        
        for i in range(len(self.rename_list)):
            print(self.rename_list[i])

        self.home()
        
    def convert_files(self):

        #start point for episode number
        i = 1

        for file in os.listdir(self.dir_):

            #Get the file extension
            file_token = file.split('.')
            file_t_len = len(file_token)
            self.format = '.' + file_token[file_t_len -1]

            #Select format for episode
            if i <= 9:
                episode = "E0" + str(i)
            else:
                episode = "E" + str(i)
            
            new_name = self.name + " " + self.season + episode +  " - " + self.rename_list[i-1] + self.format

            #Complete full path for file to be renamed
            new_file = os.path.join(self.dir_, file)
            
            #Rename the file
            os.rename(new_file, new_name)

            #Print old and new name of file
            print(file)
            print(new_name)
            i+=1
        
    def home(self):

        #Create some functionality to GUI
        #Labels
        self.label_series = QtGui.QLabel("Not Selected", self)
        self.label_series.move(300, 10)
        self.label_season = QtGui.QLabel("Not Selected", self)
        self.label_season.move(300, 45)
        self.label_format = QtGui.QLabel("Not Selected", self)
        self.label_format.move(300, 80)
        #buttons
        self.btn = QtGui.QPushButton("Select Series", self)
        self.btn.move(400, 10)
        self.btn.clicked.connect(self.get_text)
        self.btn = QtGui.QPushButton("Select Season", self)
        self.btn.move(400, 45)
        self.btn.clicked.connect(self.get_season)
        self.btn = QtGui.QPushButton("Select Format", self)
        self.btn.move(400, 80)
        self.btn.clicked.connect(self.get_format)
        self.btn_convert = QtGui.QPushButton("Convert", self)
        self.btn_convert.move(400, 250)
        self.btn_convert.clicked.connect(self.convert_files)
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

    def get_format(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Text Input Dialog', 'Enter The Series:')
	
        if ok:
            self.label_format.setText(str(text))
            self.format = str(text)
        
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
        
