class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

<<<<<<< HEAD
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
=======
    def __lt__(self, obj):
        return self.age < obj.age
    
    def __gt__(self, obj):
        return self.age > obj.age
    
>>>>>>> ce1c32dc5cddef4fb5baec90621882a0f53403ac

class Employee(Person):
    def __init__(self, n, a, s, l):
        super().__init__(n, a)
        self.salary = s
        self.lavozim = l
    
    def __lt__(self, obj):
        return self.salary < obj.salary
    
    def __gt__(self, obj):
        return self.salary > obj.salary

    def __add__(self, n):
        self.salary += n

e1 = Employee("jon", 20, 1500, "Manager")
e2 = Employee("Piter", 40, 500, "Adminstrator")

e1 + 500
print(e1 > e2)
print(e1.salary)






















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