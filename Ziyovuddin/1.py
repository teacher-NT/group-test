import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtCore import Qt

class DijitalSoat(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dijital Soat')
        self.setGeometry(800, 500, 250, 100)
        self.setStyleSheet("background-color: black; color: white;")

        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        
        asosiy_dizayn = QVBoxLayout()
        self.soat_matni = QLabel()
        asosiy_dizayn.addWidget(self.soat_matni)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.soatni_yangilash)
        self.timer.start(1000)
        
        self.soatni_yangilash()
        self.setLayout(asosiy_dizayn)

    def soatni_yangilash(self):
        hozirgi_vaqt = QDateTime.currentDateTime().toString("dd.MM.yyyy HH:mm:ss")
        self.soat_matni.setStyleSheet("color: red; font-size: 40px;")
        self.soat_matni.setText(hozirgi_vaqt)

if __name__ == '__main__':
    dastur = QApplication(sys.argv)
    soat_dasturi = DijitalSoat()
    soat_dasturi.show()
    sys.exit(dastur.exec())
