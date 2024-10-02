
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow,
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