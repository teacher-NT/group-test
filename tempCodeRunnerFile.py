from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QTextEdit,
    QHBoxLayout, QVBoxLayout
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
        # self.btn.move(50, 100)
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
        self.label.setFixedSize(1200, 720)

win = Window("OOP", 800, 600)
win.show()




app.exec_()