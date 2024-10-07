from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QMessageBox
)
from PyQt5.QtGui import QFont
from random import shuffle
from PyQt5.QtCore import QTimer, QTime

font = QFont("Arial", 14)
app = QApplication([])

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Raqamlar o'yini")
        self.setStyleSheet("background: aquamarine;")

        self.main_layout = QVBoxLayout()
        self.buttuns_layout = QGridLayout()
        self.control_layout = QHBoxLayout()
        
        self.timer_label = QLabel("Qolgan vaqt: 05:00")
        self.timer_label.setFont(font)
        self.main_layout.addWidget(self.timer_label)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 5, 0)  # 5 minutes countdown

        self.buttons()
        self.control()

        self.main_layout.addLayout(self.buttuns_layout)
        self.main_layout.addLayout(self.control_layout)
        self.setLayout(self.main_layout)
        self.show()
        self.check_game()

    def buttons(self):
        self.btn_list = []
        index = 0
        number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, '')
        for q in range(1, 5):
            for u in range(1, 5):
                btn = QPushButton(str(number[index]), clicked=self.game_control)
                btn.setFixedSize(70, 70)
                btn.setFont(font)
                btn.setStyleSheet("background: ivory")
                btn.setEnabled(False)
                self.btn_list.append(btn)
                self.buttuns_layout.addWidget(btn, q, u)
                index += 1

    def control(self):
        self.START = QPushButton("START", clicked=self.start_game)
        self.EXIT = QPushButton("EXIT", clicked=exit)
        self.FINISH = QPushButton("FINISH", clicked=self.finish_game)
        self.FINISH.hide()
        self.control_layout.addWidget(self.START)
        self.control_layout.addWidget(self.EXIT)
        self.control_layout.addWidget(self.FINISH)
    
    def start_game(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, '']
        shuffle(numbers)
        for i in range(len(numbers)):
            self.btn_list[i].setText(str(numbers[i]))
            self.btn_list[i].setEnabled(True)
        self.START.hide()
        self.EXIT.hide()
        self.FINISH.show()

        # Start the timer
        self.time_remaining = QTime(0, 5, 0)
        self.timer.start(1000)

    def finish_game(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, '']
        for i in range(len(numbers)):
            self.btn_list[i].setText(str(numbers[i]))
            self.btn_list[i].setEnabled(False)
        self.START.show()
        self.EXIT.show()
        self.FINISH.hide()

        # Stop the timer
        self.timer.stop()
        self.timer_label.setText("Qolgan vaqt: 05:00")

    def game_control(self):
        btn = self.sender()
        index = self.btn_list.index(btn)
        if btn.text():
            neighbors = self.get_neighbors(index)
            for neighbor_index in neighbors:
                if self.btn_list[neighbor_index].text() == "":
                    self.btn_list[neighbor_index].setText(btn.text())
                    btn.setText("")
                    break
        self.check_game()

    def get_neighbors(self, index):
        neighbors = []
        if index % 4 != 0:
            neighbors.append(index - 1)  
        if index % 4 != 3:
            neighbors.append(index + 1)  
        if index - 4 >= 0:
            neighbors.append(index - 4)  
        if index + 4 < 16:
            neighbors.append(index + 4) 
        return neighbors

    def check_game(self):
        for i in range(15):
            if self.btn_list[i].text() == str(i + 1):
                self.btn_list[i].setStyleSheet("background: lightgreen")
            else:
                self.btn_list[i].setStyleSheet("background: lightcoral")

        if all(self.btn_list[i].text() == str(i + 1) for i in range(15)) and self.btn_list[15].text() == "":
            self.timer.stop()
            self.message = QMessageBox()
            self.message.setText("Tabriklaymiz! Siz yutdingiz.")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.exec_()

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        self.timer_label.setText(f"Qolgan vaqt: {self.time_remaining.toString('mm:ss')}")
        if self.time_remaining == QTime(0, 0, 0):
            self.timer.stop()
            self.finish_game()
            QMessageBox.warning(self, "Vaqt tugadi", "Vaqt tugadi! Siz o'yinni tugata olmadingiz.")

win = Game()
app.exec_()
