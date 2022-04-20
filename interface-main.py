from fileinput import close
import sys 
from PyQt5 import QtWidgets
import matrix, information, settings, rules, assignments

class App(QtWidgets.QMainWindow, matrix.Ui_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.button_info.clicked.connect(self.info)
        self.button_settings.clicked.connect(self.settings)
        self.button_exit.clicked.connect(self.close)
        self.button_play.clicked.connect(self.play)
        self.button_assignment.clicked.connect(self.assignments)
        self.button_rules.clicked.connect(self.rules)

    def rules(self):
        window = Rules()
        window.show()
        window.exec()

    def assignments(self):
        window = Assignments()
        window.show()
        window.exec()

    def play(self):
        pass

    def settings(self):
        window = Settings()
        window.show()
        window.exec()
    
    def info(self):
        window = Information()
        window.show()
        window.exec()

class Information(QtWidgets.QDialog, information.Ui_DInfo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)

class Settings(QtWidgets.QDialog, settings.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

class Rules(QtWidgets.QDialog, rules.Ui_rules):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

class Assignments(QtWidgets.QDialog, assignments.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = App()  
    window.show() 
    app.exec_() 

if __name__ == '__main__':  
    main()  