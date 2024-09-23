from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def turn(self):
        pass

class BMW(Player):

    def __init__(self, nom, rang, max_speed):
        self.name = nom
        self.color = rang
        self.max_speed = max_speed

    def run(self):
        print("Running")

    def turn(self):
        print("Turn around")

b = BMW("R8", "Qora", 260)

print(b.max_speed)

