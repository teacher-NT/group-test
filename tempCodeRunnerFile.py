<<<<<<< HEAD
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder  
        self.__balance = 1000            

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
=======
    @abstractmethod
    def turn(self):
        pass