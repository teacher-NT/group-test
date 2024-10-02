class Plane:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("Uchyapman")
        
class Property(Plane):
    def __init__(self, name):
        self.name = name
    def move(self):
        print("Yuqorida uchayapman")

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
d = Property("Tezkor samalyot")
a.move()
b.move()
c.move()
d.move()