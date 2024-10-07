import time
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import shuffle
import pygame
font = QFont("Arial", 14)
app = QApplication([])

pygame.mixer.init()
pygame.mixer.music.load('papyrus.ogg')
pygame.mixer.music.play(5+5)

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Raqamlar o'yini")
        self.setStyleSheet("background: #000000;")
        self.main_layout = QVBoxLayout()
        self.buttuns_layout = QGridLayout()
        self.control_layout = QHBoxLayout()

        self.timer_label = QLabel("Time left: 5:00")
        self.timer_label.setFont(font)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.timer_label)

        self.buttons()
        self.control()

        self.main_layout.addLayout(self.buttuns_layout)
        self.main_layout.addLayout(self.control_layout)
        self.setLayout(self.main_layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)  # <-- BU YERDA 'update_timer' metodini chaqiryapmiz
        self.time_left = 1  
        self.show()

    def buttons(self):
        self.btn_list = []
        index = 0
        number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, '')
        for q in range(1, 5):
            for u in range(1, 5):
                btn = QPushButton(str(number[index]), clicked=self.game_control)
                btn.setFixedSize(70, 70)
                btn.setFont(font)
                btn.setStyleSheet("background: #FF0000")
                btn.setEnabled(False)
                self.btn_list.append(btn)
                self.buttuns_layout.addWidget(btn, q, u)
                index += 1

    def control(self):
        self.START = QPushButton("START", clicked=self.start_game)
        self.START.setStyleSheet("background: #33FF00;")
        self.EXIT = QPushButton("EXIT", clicked=self.ee)
        self.EXIT.setStyleSheet("background: #FF3333;")
        self.FINISH = QPushButton("FINISH", clicked=self.finish_game)
        self.FINISH.setStyleSheet("background: #FF3333;")
        self.FINISH.hide()
        self.control_layout.addWidget(self.START)
        self.control_layout.addWidget(self.EXIT)
        self.control_layout.addWidget(self.FINISH)
    
    def ee(self):
        pygame.mixer.init()
        pygame.mixer.music.load('gameover.ogg')
        pygame.mixer.music.play()
        time.sleep(1.5)
        quit()

    def start_game(self):
        pygame.mixer.init()
        pygame.mixer.music.play()
        time.sleep(2)
        pygame.mixer.init()
        pygame.mixer.music.load('prebattle1.ogg')
        pygame.mixer.music.play()
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, '']
        shuffle(numbers)
        for i in range(len(numbers)):
            self.btn_list[i].setText(str(numbers[i]))
            self.btn_list[i].setEnabled(True)
        self.START.hide()
        self.EXIT.hide()
        self.FINISH.show()
        self.time_left = 300  
        self.timer.start(1000) 

    def finish_game(self):
        pygame.mixer.init()
        pygame.mixer.music.load('golos-knopka.mp3')
        pygame.mixer.music.play()
        time.sleep(2)
        pygame.mixer.init()
        pygame.mixer.music.load('papyrus.ogg')
        pygame.mixer.music.play()
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, '']
        for i in range(len(numbers)):
            self.btn_list[i].setText(str(numbers[i]))
            self.btn_list[i].setEnabled(False)
        
        self.START.show()
        self.EXIT.show()
        self.FINISH.hide()
        self.timer.stop()
        msg_box = QMessageBox()
        msg_box.setWindowTitle("O'yin tugadi")
        msg_box.setText("O'yin tugadi! Siz yutqazdingiz.")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.timer_label.setText(f"Time left: {minutes:02}:{seconds:02}")
            for i in range(15):  
                if self.btn_list[i].text() == str(i + 1):  
                    self.btn_list[i].setStyleSheet("background-color: 33FF00")  
                else:
                    self.btn_list[i].setStyleSheet("background-color: #FF0000")  
        else:
            self.timer.stop()
            self.timer_label.setText("Vaqt tugadi! Siz yutqazdingiz!")
            self.setStyleSheet("background-color: red;")  
            self.timer_label.setStyleSheet("color: black;")  
            self.finish_game()
        if all(btn.text() == str(i + 1) for i, btn in enumerate(self.btn_list[:-1])) and self.btn_list[-1].text() == '':
            self.timer.stop()
            self.timer_label.setText("Tabriklaymiz! Siz g'alaba qozondingiz!")
            self.finish_game()
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
            if self.btn_list[6] =='6':
                self.btn_list[6] = self.setStyleSheet("backround-color: green")
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
if __name__ == "__main__":
    window = Game()
    app.exec_()
