import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QVBoxLayout, QComboBox, QMessageBox
)
from PyQt5.QtGui import QFont


with open("bank.json", "r", encoding="utf-8") as f:
    data = json.load(f)

app = QApplication([])

font = QFont("Arial", 14)

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Valyuta Konverteri")
        self.setFixedSize(800, 600)

        
        layout = QVBoxLayout()
        self.setStyleSheet("background-color: cyan;colour-white")

       
        self.label = QLabel("Valyutani tanlang:", self)
        self.label.setGeometry(400,350,200,50)
        self.label.setFont(font)
        layout.addWidget(self.label)

        
        self.currency_menu = QComboBox(self)
        self.currency_menu.setFont(font)
        
        for currency in data:
            self.currency_menu.addItem(f"{currency['title']} ({currency['code']})", currency)
        layout.addWidget(self.currency_menu)

        
        self.amount_input = QLineEdit(self)
        self.amount_input.setFont(font)
        self.amount_input.setPlaceholderText("Miqdorni kiriting")
        layout.addWidget(self.amount_input)

        
        self.convert_button = QPushButton("Hisoblash", self)
        self.convert_button.setFont(font)
        self.convert_button.clicked.connect(self.calculate)
        layout.addWidget(self.convert_button)

        
        self.result_label = QLabel("", self)
        self.result_label.setFont(font)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        
        selected_currency = self.currency_menu.currentData()
        amount_text = self.amount_input.text()

       
        try:
            amount = float(amount_text)
        except ValueError:
            QMessageBox.warning(self, "Xato", "Iltimos, to'g'ri miqdor kiriting!")
            return

        
        cb_price = float(selected_currency['cb_price'])  # Markaziy bank kursi
        nbu_buy_price = selected_currency['nbu_buy_price']
        nbu_sell_price = selected_currency['nbu_cell_price']

        
        som_amount_cb = amount * cb_price
        result_text = f"Markaziy bank kursi bo'yicha: {som_amount_cb:.2f} so'm\n"

        if nbu_buy_price and nbu_sell_price:
            som_amount_nbu_buy = amount * float(nbu_buy_price)
            som_amount_nbu_sell = amount * float(nbu_sell_price)
            result_text += f"Mablag' sotib olish kursi bo'yicha: {som_amount_nbu_buy:.2f} so'm\n"
            result_text += f"Mablag' sotish kursi bo'yicha: {som_amount_nbu_sell:.2f} so'm"

        self.result_label.setText(result_text)


window = CurrencyConverter()
window.show()

app.exec_()
