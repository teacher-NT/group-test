class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} so'm depozit qilindi. Joriy balans: {self.__balance} so'm")
        else:
            print("Depozit miqdori musbat bo'lishi kerak.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} so'm yechildi. Joriy balans: {self.__balance} so'm")
        else:
            print("Yetarli mablag' mavjud emas yoki miqdor noto'g'ri.")


my_account = BankAccount("12345678", 1000)
my_account.deposit(500)  
my_account.withdraw(300)  
print(f"Joriy balans: {my_account.balance} so'm")  

