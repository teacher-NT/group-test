class Animal:
    def  __init__(self, n):
        self.name = n
    def eat(self, meal):
        print(f"Men {meal} yemoqdaman!")

class Dog(Animal):
    def __init__(self, n, z, r, y):
        self.zot = z
        self.rang = r
        self.yosh = y
        super().__init__(n)
    def eat(self, meal, drink):
        print(f"{self.name} {meal} yeydi va {drink} ichadi!")

class Cat(Animal):
    pass

d1 = Dog("Tom", "Chihiahia", "sariq", 5)
c1 = Cat("Baroq")

d1.eat("go'sht", "cola")
print(d1.zot, d1.rang, d1.yosh)
# c1.eat("baliq")