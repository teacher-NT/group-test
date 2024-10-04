from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QTextEdit,
    QHBoxLayout, QVBoxLayout,
    QMessageBox, QComboBox, QCheckBox,  QRadioButton
)
from PyQt5.QtGui import QFont
font = QFont("Arial", 14)

app = QApplication([])

class Window2(QWidget):
    def  __init__(self, name, num):
        super().__init__()
        self.setWindowTitle(name)
        # self.setFixedSize(200, 200)
        self.setGeometry(200, 200, 400, 300)
        self.label = QLabel(self)
        self.label.setText(f"Bu {num}-oyna")
        self.btn = QPushButton("Exit", self, clicked=self.hide)
        self.show()

class Window(QWidget):
    def __init__(self, title, width, height):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setWindowTitle(title)  
        self.setFixedSize(width, height)
        self.oynalar = []
        self.count = 0
        self.btn = QPushButton("New", self,  clicked=self.new)
        # self.btn.setText("New")
        # self.btn.clicked.connect
        self.setLayout(self.layout)
    def new(self):
        self.count +=  1
        win = Window2("Yangi oyna", self.count)
        self.oynalar.append(win)
    
win = Window("OOP", 800, 600)
win.show()

app.exec_()

















<<<<<<< HEAD
=======


>>>>>>> 36ec3b8326ec79aab120c7ebcb4a1b6d6987a8
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