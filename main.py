class Plane:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("Uchyapman")

class Car:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("Yuryapman")

class Boat:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("Suzyapman")


a = Plane("Samalyot")
b = Car("Mashina")
c = Boat("Qayiq")
a.move()
b.move()
c.move()


























"""
Abstraktsiya
"""
# from abc import ABC, abstractmethod

# class Player(ABC):
#     @abstractmethod
#     def run(self):
#         pass

#     @abstractmethod
#     def turn(self):
#         pass
    
#     @abstractmethod
#     def stop(self):
#         pass
    
# class BMW(Player):

#     def __init__(self, nom, rang, max_tezlik):
#         self.name = nom
#         self.color = rang
#         self.max_speed = max_tezlik

#     def run(self):
#         print("Running")

#     def turn(self):
#         print("Turn around")
        
#     def stop(self):
#         print("Stop now")

# b = BMW("R8", "black", 260)

# print(b.max_speed)
# print(b.name)
# print(b.color)



# my_account = BankAccount("Elon Musk")
# print(my_account.get_balance()) 
# my_account.deposit(-200)  
# my_account.withdraw(5000)  