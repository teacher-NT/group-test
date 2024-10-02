
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QTextEdit,
    QHBoxLayout, QVBoxLayout,
    QMessageBox, QComboBox, QCheckBox,  QRadioButton
)
from PyQt5.QtGui import QFont
font = QFont("Arial", 14)

app = QApplication([])

class Window(QWidget):
    def __init__(self,title, width, height):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setWindowTitle(title)
        self.setFixedSize(width, height)
        # self.show_checklist() 
        # self.show_menu()
        self.show_radio()
        self.setLayout(self.layout)
    
    def show_radio(self):
        male = QRadioButton(self)
        male.setText("Erkak")

        female = QRadioButton(self)
        female.setText("Ayol")

        self.layout.addWidget(male)
        self.layout.addWidget(female)

    def show_checklist(self):
        self.checkList = QCheckBox(self)
        self.checkList.setText("Qiyma")

        self.checkList2 = QCheckBox(self)
        self.checkList2.setText("Jaz")

        self.checkList3 = QCheckBox(self)
        self.checkList3.setText("Tovuq")

        self.layout.addWidget(self.checkList)
        self.layout.addWidget(self.checkList2)
        self.layout.addWidget(self.checkList3)

    def show_menu(self):
        self.menu = QComboBox(self)
        self.menu.addItems(["Lavash", "HotDog", "Pizza", "Sho'rva", "Free", "Osh", "Shashlik"])
        # self.menu.addItem("Lavash")
        # self.menu.addItem("HotDog")
        self.layout.addWidget(self.menu)

    def lb(self):
        self.label = QLabel(self)
        self.label.setText("Menyu:")
        self.label.setFont(font)

        self.btn = QPushButton(self)
        self.btn.setText("Zoom")
        self.btn.clicked.connect(self.func)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn)

    def func(self):
        choice = self.menu.currentText()
        tur = self.checkList.text()

        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setText(f"Siz {tur} {choice} tanladingiz!")  
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()

win = Window("OOP", 800, 600)
win.show()




app.exec_()














