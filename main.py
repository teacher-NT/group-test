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
    
    @abstractmethod
    def stop(self):
        pass
    
class BMW(Player):

    def __init__(self, nom, rang, max_tezlik):
        self.name = nom
        self.color = rang
        self.max_speed = max_tezlik

    def run(self):
        print("Running")

    def turn(self):
        print("Turn around")
        
    def stop(self):
        print("Stop now")

b = BMW("R8", "black", 260)

print(b.max_speed)
print(b.name)
print(b.color)

>>>>>>> 928db268fd734e5d5b81b35eb1d0f20b222d2be2


my_account = BankAccount("Elon Musk")
print(my_account.get_balance()) 
my_account.deposit(-200)  
my_account.withdraw(5000)  