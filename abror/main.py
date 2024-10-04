from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

def on_button_click():
    label.setText("Tugma bosildi!")

app = QApplication([])

window = QWidget()
window.setWindowTitle("Dastur Sarlavhasi")
window.setFixedSize(400, 300)

layout = QVBoxLayout()
label = QLabel("Salom, Dunyo!")
button = QPushButton("Meni bosing!")

layout.addWidget(label)
layout.addWidget(button)

button.clicked.connect(on_button_click)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
