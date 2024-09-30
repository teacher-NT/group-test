# #print("hello")
# # import googletrans

# # translator = googletrans.Translator()

# # text = input("Enter text: ")

# # result = translator.translate(text, dest="en")

# # print(result.text)
# import os

# os.system('cls' if os.name == 'nt' else 'clear')


from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QTextEdit,
    QHBoxLayout, QVBoxLayout,
    QMessageBox,QComboBox
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
        self.label.setText("menu")
        self.label.setFont(font)

        self.btn = QPushButton(self)
        self.btn.setText("Zoom")
        self.btn.clicked.connect(self.func)

    
        self.menu=QComboBox(self)
        # self.menu.addItem("lavash")
        # self.menu.addItem("hotdog")
        self.menu.addItems(['lavash','osh','hotdog','cola'])

        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        # layout.addWidget(self.btn1)
        # layout.addWidget(self.btn2)
        # layout.addWidget(self.btn3)
        layout.addWidget(self.menu)
        self.setLayout(layout)

    def func(self):
        choice=self.menu.currentText()
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("message")
        msg.setText(f"siz {choice}ni tanladingiz")  
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()

win = Window("OOP", 800, 600)
win.show()




app.exec_()
