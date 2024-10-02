from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QTextEdit,
    QHBoxLayout, QVBoxLayout,
    QMessageBox, QComboBox
)
from PyQt5.QtGui import QFont
font = QFont("Arial", 14)

app = QApplication([])

class Window(QWidget):
    def __init__(self,title, width, height):
        super().__init__()

        layout = QVBoxLayout()
        self.setWindowTitle(title)
        self.setFixedSize(width, height)
        self.label = QLabel(self)
        self.label.setText("Menyu:")
        self.label.setFont(font)

        self.btn = QPushButton(self)
        self.btn.setText("Zoom")
        self.btn.clicked.connect(self.func)
       
        self.menu = QComboBox(self)
        self.menu.addItems(["Lavash", "HotDog", "Pizza", "Sho'rva", "Free", "Osh", "Shashlik"])
        # self.menu.addItem("Lavash")
        # self.menu.addItem("HotDog")

        layout.addWidget(self.label)
        layout.addWidget(self.menu)
        layout.addWidget(self.btn)
        
        
        self.setLayout(layout)

    def func(self):
        choice = self.menu.currentText()
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setText(f"Siz {choice} tanladingiz!")  
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()

win = Window("OOP", 800, 600)
win.show()




app.exec_()