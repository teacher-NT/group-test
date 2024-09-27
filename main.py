from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QTextEdit
)
from PyQt5.QtGui import QFont
font = QFont("Arial", 14)

app = QApplication([])

win = QWidget()
win.setGeometry(100, 100, 1200, 720)
win.setWindowTitle("Mening birinchi Interfeys dasturim")

label = QLabel(win)
label.setText("Salom hammaga")
label.setFont(font)
# label.setFixedSize(400, 50)
# label.setStyleSheet("font-size: 40px; color: blue;")

# line = QLineEdit(win)
# line.setGeometry(0, 100, 200, 50)
# line.setFont(font)
text = QTextEdit(win)
text.setGeometry(0, 100, 400, 300 )

def func():
    t = text.toPlainText()
    t = t.upper()
    label.setText(f"Salom {t}")

btn = QPushButton(win)
btn.setText("Meni bos!")
btn.setFont(font)
btn.setGeometry(0, 400, 200, 50)
btn.clicked.connect(func)

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