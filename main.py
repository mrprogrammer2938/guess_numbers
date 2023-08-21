#!/usr/bin/python3
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

import sys,random

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("number_guess.ui",self)
        self.setWindowTitle("بازی حدس اعداد")
        self.setGeometry(500,200,420,311)
        self.setFixedSize(420,311)
        self.start_btn.clicked.connect(self.sg)
        self.exit_btn.clicked.connect(self.close)
    def sg(self):
        self.get_number()
        self.start_game()
    def sg_2(self):
        self.w3.close()
        self.get_number()
        self.start_game()
    def get_number(self):
        self.random_number = random.randint(0,10)
       
                
    def start_game(self):
        self.w = QDialog(self)
        loadUi("number_guess_dialog.ui",self.w)
        self.w.setGeometry(950,200,400,300)
        self.w.save_btn.clicked.connect(self.check_number)
        self.w.back_btn.clicked.connect(self.w.close)
        
        self.w.setWindowTitle("بازی حدس اعداد")
        self.w.show()
    def start_game_2(self):
        self.w2.close()
        self.start_game()  
    def check_number(self):
        user_number = int(self.w.number.text())
        if user_number == self.random_number:
            self.winner()
        else:
            self.lose()
            
    def winner(self):
        self.w.close()
        self.w3 = QDialog(self)
        self.w3.setGeometry(950,200,400,300)
        self.w3.setFixedSize(400,300)
        loadUi("number_guess_winner.ui",self.w3)
        self.w3.start_btn.clicked.connect(self.sg_2)
        self.w3.exit_btn.clicked.connect(self.exit_game)
        self.w3.show()
    def exit_game(self):
        self.w3.close()
        self.close()
    
    def lose(self):
        self.w.close()
        self.w2 = QDialog(self)
        loadUi("number_guess_error.ui",self.w2)
        self.w2.setGeometry(950,200,470,300)
        self.w2.setFixedSize(470,300)
        self.w2.try_again.clicked.connect(self.start_game_2)
        self.w2.back_btn.clicked.connect(self.w2.close)
        self.w2.show()
        
def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    