from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow,
    QPushButton, QLineEdit, QTextEdit,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QMessageBox, QComboBox, QCheckBox,  QRadioButton
)
from PyQt5.QtGui import QFont
from random import shuffle
from PyQt5.QtCore import (QTimer,Qt)

font = QFont("Arial", 14)
app = QApplication([])

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Raqamlar o'yini")
        self.setStyleSheet("background: gray;")

        self.main_layout = QVBoxLayout()
        self.buttuns_layout = QGridLayout()
        self.control_layout = QHBoxLayout()
        self.label=QLabel("1 daqiqa vaqtingiz bor")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background:blue;color:red;font-size:18px;")
        self.main_layout.addWidget(self.label)
        self.label.hide()
        self.buttons()
        self.control()

        self.main_layout.addLayout(self.buttuns_layout)
        self.main_layout.addLayout(self.control_layout)
        self.setLayout(self.main_layout)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_up)
        self.time_remaining = 60  # Game duration in seconds
        self.show()
        
    def buttons(self):
        self.btn_list = []
        index = 0
        number = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'')
        for q in range(1, 5):
            for u in range(1, 5):
                btn = QPushButton(str(number[index]), clicked=self.game_control)
                btn.setFixedSize(70, 70)
                btn.setFont(font)
                btn.setStyleSheet("background: #a1d6d5")
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
        self.label.show()
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'']
        shuffle(numbers)
        for i in range(len(numbers)):
            self.btn_list[i].setText(str(numbers[i]))
            self.btn_list[i].setEnabled(True)
        self.START.hide()
        self.EXIT.hide()
        self.FINISH.show()
        self.time_remaining = 60
        self.label.setText("1 daqiqa vaqtingiz bor")
        self.timer.start(1000)
    
    def finish_game(self):
        self.timer.stop()
        self.label.hide()
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'']
        for i in range(len(numbers)):
            self.btn_list[i].setText(str(numbers[i]))
            self.btn_list[i].setEnabled(False)
        self.START.show()
        self.EXIT.show()
        self.FINISH.hide()

    def time_up(self):
        self.time_remaining -= 1
        self.label.setText(f"Qolgan vaqt: {self.time_remaining} soniya")
        if self.time_remaining <= 0:
            self.timer.stop()
            self.label.setText("Vaqt tugadi!")
            QMessageBox.warning(self, "Vaqt tugadi", "O'yin tugadi, vaqtingiz tugadi.")
            self.finish_game()

    def game_control(self):
        btn = self.sender()
        text = btn.text()

        # Only move if the button text is not empty and adjacent to the empty space
        if text:
            current_idx = self.btn_list.index(btn)
            empty_idx = self.btn_list.index(self.find_empty_button())

            if self.is_adjacent(current_idx, empty_idx):
                self.btn_list[empty_idx].setText(text)
                btn.setText('')
        
        self.check_game()

    def find_empty_button(self):
        # Finds the button with empty text
        for btn in self.btn_list:
            if btn.text() == '':
                return btn

    def is_adjacent(self, idx1, idx2):
        # Check if two buttons are adjacent (horizontally or vertically)
        row1, col1 = divmod(idx1, 4)
        row2, col2 = divmod(idx2, 4)
        return abs(row1 - row2) + abs(col1 - col2) == 1

    def check_game(self):
        n = 0
        for i in range(1, 16):
            if self.btn_list[i-1].text() == str(i):
                n += 1
        if n == 15:
            self.timer.stop()
            self.label.hide()
            QMessageBox.information(self, "Tabriklaymiz", "Siz o'yinni muvaffaqiyatli tugatdingiz!")

win = Game()

app.exec_()
