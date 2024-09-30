from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QTextEdit,
    QHBoxLayout, QVBoxLayout,
    QMessageBox
)
from PyQt5.QtGui import QFont
font = QFont("Arial", 14)

app = QApplication([])

class Window(QWidget):
    def __init__(self,title, width, height):
        super().__init__()

        layout = QVBoxLayout()
        self.setWindowTitle(title)
        # self.setFixedSize(width, height)
        self.label = QLabel(self)
        self.label.setText("Bu label")
        self.label.setFont(font)

        self.btn = QPushButton(self)
        self.btn.setText("Zoom")
        self.btn.clicked.connect(self.func)

        self.btn1 = QPushButton(self)
        self.btn1.setText("Zoom")
       

        self.btn2 = QPushButton(self)
        self.btn2.setText("Zoom")

        self.btn3 = QPushButton(self)
        self.btn3.setText("Zoom")
       

        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        
        self.setLayout(layout)

    def func(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setText("Bu ogohlantirish xabari")  
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()

win = Window("OOP", 800, 600)
win.show()

app.exec_()


















"""
Abstraktsiya
"""
# from abc import ABC, abstractmethod

# class Player(ABC):
#     @abstractmethod
#     def run(self):
#         pass

#     @abstractmethod
#     def turn(self):
#         pass
    
#     @abstractmethod
#     def stop(self):
#         pass
    
# class BMW(Player):

#     def __init__(self, nom, rang, max_tezlik):
#         self.name = nom
#         self.color = rang
#         self.max_speed = max_tezlik

#     def run(self):
#         print("Running")

#     def turn(self):
#         print("Turn around")
        
#     def stop(self):
#         print("Stop now")

# b = BMW("R8", "black", 260)

# print(b.max_speed)
# print(b.name)
# print(b.color)

# my_account = BankAccount("Elon Musk")
# print(my_account.get_balance()) 
# my_account.deposit(-200)  
# my_account.withdraw(5000)  