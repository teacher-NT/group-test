from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow,
    QPushButton, QLineEdit, QTextEdit,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QMessageBox, QComboBox, QCheckBox,  QRadioButton
)
from PyQt5.QtGui import QFont
from random import shuffle
import pygame
import time

font = QFont("Papyrus", 15)
app = QApplication([])

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Raqamlar o'yini")
        self.setStyleSheet("background: grey;")

        self.main_layout = QVBoxLayout()
        self.buttuns_layout = QGridLayout()
        self.control_layout = QHBoxLayout()

        self.buttons()
        self.control()
        
        self.main_layout.addLayout(self.buttuns_layout)
        self.main_layout.addLayout(self.control_layout)
        self.setLayout(self.main_layout)
        self.show()
        # self.check_game()

    def buttons(self):
        self.btn_list = []
        index = 0
        number = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'')
        for q in range(1, 5):
            for u in range(1, 5):
                btn = QPushButton(str(number[index]), clicked=self.game_control)
                btn.setFixedSize(70, 70)
                btn.setFont(font)
                btn.setStyleSheet("background: white;border-radius:8px;border: 2px solid brown")
                btn.setEnabled(False)
                self.btn_list.append(btn)
                self.buttuns_layout.addWidget(btn, q, u)
                index += 1

    def control(self):
        self.START = QPushButton("START", clicked=self.start_game)
        
        self.START.setStyleSheet("""
              QPushButton {
                background-color: grey; 
                color: black; 
                border-radius: 15px; 
                padding: 10px; 
                border: 2px solid brown; 
                font-size: 14px; 
            }
            QPushButton:hover {
                background-color: lightgreen; 
                border: 2px solid green; 
            }
        """)
        self.START.setFont(font)
        self.EXIT = QPushButton("EXIT", clicked=exit)
        self.EXIT.setStyleSheet("""
              QPushButton {
                background-color: grey; 
                color: black; 
                border-radius: 15px; 
                padding: 10px; 
                border: 2px solid brown; 
                font-size: 14px; 
            }
            QPushButton:hover {
                background-color: red; 
                border: 2px solid red;         
            }
        """)
        self.EXIT.setFont(font)
        self.FINISH = QPushButton("FINISH", clicked=self.finish_game)
        self.FINISH.setStyleSheet("""
              QPushButton {
                background-color:  grey;
                color: black; 
                border-radius: 15px; 
                padding: 10px; 
                border: 2px solid brown; 
                font-size: 14px; 
            }
            QPushButton:hover {
                background-color: orange; 
                border: 2px solid yellow; 
            }
        """)
        self.FINISH.setFont(font)
        self.FINISH.hide()
        self.control_layout.addWidget(self.START)
        self.control_layout.addWidget(self.EXIT)
        self.control_layout.addWidget(self.FINISH)
    
    def start_game(self):
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'']
        shuffle(numbers)
        for i in range(len(numbers)):
            self.btn_list[i].setText(str(numbers[i]))
            self.btn_list[i].setEnabled(True)
            self.btn_list[i].setFont(font)
            
        self.START.hide()
        self.EXIT.hide()
        self.FINISH.show()
        
    
    def finish_game(self):
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'']
        for i in range(len(numbers)):
            self.btn_list[i].setText(str(numbers[i]))
            self.btn_list[i].setEnabled(False)
        self.START.show()
        self.EXIT.show()
        self.FINISH.hide()

    def game_control(self):
        btn = self.sender()
        text = btn.text()
        if text and btn == self.btn_list[0]:
            if self.btn_list[1].text() == "":
                self.btn_list[0].setText(self.btn_list[1].text())
                self.btn_list[1].setText(text)
            elif self.btn_list[4].text() == "":
                self.btn_list[0].setText(self.btn_list[4].text())
                self.btn_list[4].setText(text)
        elif text and btn == self.btn_list[1]:
            if self.btn_list[0].text() == "":
                self.btn_list[1].setText(self.btn_list[0].text())
                self.btn_list[0].setText(text)
            elif self.btn_list[2].text() == "":
                self.btn_list[1].setText(self.btn_list[2].text())
                self.btn_list[2].setText(text)
            elif self.btn_list[5].text() == "":
                self.btn_list[1].setText(self.btn_list[5].text())
                self.btn_list[5].setText(text)

        elif text and btn == self.btn_list[2]:
            if self.btn_list[1].text() == "":
                self.btn_list[2].setText(self.btn_list[1].text())
                self.btn_list[1].setText(text)
            elif self.btn_list[3].text() == "":
                self.btn_list[2].setText(self.btn_list[3].text())
                self.btn_list[3].setText(text)
            elif self.btn_list[6].text() == "":
                self.btn_list[2].setText(self.btn_list[6].text())
                self.btn_list[6].setText(text)
        elif text and btn == self.btn_list[3]:
            if self.btn_list[2].text() == "":
                self.btn_list[3].setText(self.btn_list[2].text())
                self.btn_list[2].setText(text)
            elif self.btn_list[7].text() == "":
                self.btn_list[3].setText(self.btn_list[7].text())
                self.btn_list[7].setText(text)
        
        elif text and btn == self.btn_list[4]:
            if self.btn_list[0].text() == "":
                self.btn_list[4].setText(self.btn_list[0].text())
                self.btn_list[0].setText(text)
            elif self.btn_list[5].text() == "":
                self.btn_list[4].setText(self.btn_list[5].text())
                self.btn_list[5].setText(text)
            elif self.btn_list[8].text() == "":
                self.btn_list[4].setText(self.btn_list[8].text())
                self.btn_list[8].setText(text)
        
        elif text and btn == self.btn_list[5]:
            if self.btn_list[1].text() == "":
                self.btn_list[5].setText(self.btn_list[1].text())
                self.btn_list[1].setText(text)
            elif self.btn_list[4].text() == "":
                self.btn_list[5].setText(self.btn_list[4].text())
                self.btn_list[4].setText(text)
            elif self.btn_list[6].text() == "":
                self.btn_list[5].setText(self.btn_list[6].text())
                self.btn_list[6].setText(text)
            elif self.btn_list[9].text() == "":
                self.btn_list[5].setText(self.btn_list[9].text())
                self.btn_list[9].setText(text)

        elif text and btn == self.btn_list[6]:
            if self.btn_list[2].text() == "":
                self.btn_list[6].setText(self.btn_list[2].text())
                self.btn_list[2].setText(text)
            elif self.btn_list[5].text() == "":
                self.btn_list[6].setText(self.btn_list[5].text())
                self.btn_list[5].setText(text)
            elif self.btn_list[7].text() == "":
                self.btn_list[6].setText(self.btn_list[7].text())
                self.btn_list[7].setText(text)
            elif self.btn_list[10].text() == "":
                self.btn_list[6].setText(self.btn_list[10].text())
                self.btn_list[10].setText(text)
        
        elif text and btn == self.btn_list[7]:
            if self.btn_list[3].text() == "":
                self.btn_list[7].setText(self.btn_list[3].text())
                self.btn_list[3].setText(text)
            elif self.btn_list[6].text() == "":
                self.btn_list[7].setText(self.btn_list[6].text())
                self.btn_list[6].setText(text)
            elif self.btn_list[11].text() == "":
                self.btn_list[7].setText(self.btn_list[11].text())
                self.btn_list[11].setText(text)

        # Diyorbekning varianti
        elif text and btn == self.btn_list[8]:
            if self.btn_list[4].text() == "":
                self.btn_list[8].setText(self.btn_list[4].text())
                self.btn_list[4].setText(text)
            elif self.btn_list[9].text() == "":
                self.btn_list[8].setText(self.btn_list[9].text())
                self.btn_list[9].setText(text)
            elif self.btn_list[12].text() == "":
                self.btn_list[8].setText(self.btn_list[12].text())
                self.btn_list[12].setText(text)
        elif text and btn == self.btn_list[9]:
            if self.btn_list[5].text() == "":
                self.btn_list[9].setText(self.btn_list[5].text())
                self.btn_list[5].setText(text)
            elif self.btn_list[8].text() == "":
                self.btn_list[9].setText(self.btn_list[8].text())
                self.btn_list[8].setText(text)
            elif self.btn_list[10].text() == "":
                self.btn_list[9].setText(self.btn_list[10].text())
                self.btn_list[10].setText(text)
            elif self.btn_list[13].text() == "":
                self.btn_list[9].setText(self.btn_list[13].text())
                self.btn_list[13].setText(text)

        elif text and btn == self.btn_list[10]:
            if self.btn_list[6].text() == "":
                self.btn_list[10].setText(self.btn_list[6].text())
                self.btn_list[6].setText(text)
            elif self.btn_list[9].text() == "":
                self.btn_list[10].setText(self.btn_list[9].text())
                self.btn_list[9].setText(text)
            elif self.btn_list[11].text() == "":
                self.btn_list[10].setText(self.btn_list[11].text())
                self.btn_list[11].setText(text)
            elif self.btn_list[14].text() == "":
                self.btn_list[10].setText(self.btn_list[14].text())
                self.btn_list[14].setText(text)
        elif text and btn == self.btn_list[11]:
            if self.btn_list[7].text() == "":
                self.btn_list[11].setText(self.btn_list[7].text())
                self.btn_list[7].setText(text)
            elif self.btn_list[10].text() == "":
                self.btn_list[11].setText(self.btn_list[10].text())
                self.btn_list[10].setText(text)
            elif self.btn_list[15].text() == "":
                self.btn_list[11].setText(self.btn_list[15].text())
                self.btn_list[15].setText(text)
        
        elif text and btn == self.btn_list[12]:
            if self.btn_list[8].text() == "":
                self.btn_list[12].setText(self.btn_list[8].text())
                self.btn_list[8].setText(text)
            elif self.btn_list[13].text() == "":
                self.btn_list[12].setText(self.btn_list[13].text())
                self.btn_list[13].setText(text)
        
        elif text and btn == self.btn_list[13]:
            if self.btn_list[9].text() == "":
                self.btn_list[13].setText(self.btn_list[9].text())
                self.btn_list[9].setText(text)
            elif self.btn_list[12].text() == "":
                self.btn_list[13].setText(self.btn_list[12].text())
                self.btn_list[12].setText(text)
            elif self.btn_list[14].text() == "":
                self.btn_list[13].setText(self.btn_list[14].text())
                self.btn_list[14].setText(text)

        elif text and btn == self.btn_list[14]:
            if self.btn_list[10].text() == "":
                self.btn_list[14].setText(self.btn_list[10].text())
                self.btn_list[10].setText(text)
            elif self.btn_list[13].text() == "":
                self.btn_list[14].setText(self.btn_list[13].text())
                self.btn_list[13].setText(text)
            elif self.btn_list[15].text() == "":
                self.btn_list[14].setText(self.btn_list[15].text())
                self.btn_list[15].setText(text)
        
        elif text and btn == self.btn_list[15]:
            if self.btn_list[11].text() == "":
                self.btn_list[15].setText(self.btn_list[11].text())
                self.btn_list[11].setText(text)
            elif self.btn_list[14].text() == "":
                self.btn_list[15].setText(self.btn_list[14].text())
                self.btn_list[14].setText(text)

    def check_game(self):
        n = 0
        for i in range(1, 16):
            if self.btn_list[i-1].text() == str(i):
                print(i, n)
                n += 1
        print(n)
        if n == 15:
            print("Ishladi")
            self.message = QMessageBox()
            self.message.setText("Tabriklaymiz! Siz yutdingiz.")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.exec_()

win = Game()

app.exec_()