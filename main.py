<<<<<<< HEAD
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder  
        self.__balance = 1000            
=======
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow,
    QPushButton, QLineEdit, QTextEdit,
    QHBoxLayout, QVBoxLayout,
    QMessageBox, QComboBox, QCheckBox,  QRadioButton
)
from PyQt5.QtGui import QFont
font = QFont("Arial", 14)
>>>>>>> 36ec3b8326ec79aab120c7ebcb4a1b6d6987a824

    def get_balance(self):
        return self.__balance

<<<<<<< HEAD
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} miqdorda depozit kiritildi. Joriy balans: {self.__balance}")
        else:
            print("Depozit miqdori noto'g'ri!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} miqdorda pul yechildi. Joriy balans: {self.__balance}")
        else:
            print("Yechish uchun balans yetarli emas yoki miqdor noto'g'ri!")


my_account = BankAccount("Elon Musk")
print(my_account.get_balance()) 
my_account.deposit(-200)  
my_account.withdraw(5000)  
=======
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

class Window(QMainWindow):
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
>>>>>>> 36ec3b8326ec79aab120c7ebcb4a1b6d6987a824
