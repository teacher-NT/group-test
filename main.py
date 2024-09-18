class Person:
    def __init__(self, n, s, a):
        self.name = n
        self.surname = s
        self.age = a

    def salom_ber(self, n):
        print(f"Salom {n}")

c1 = Person("Ibrohim", "Qo'ldoshev", 18)
c2 = Person("Diyorbek", "Turdialiyev", 19)

c1.salom_ber("Abror")
c2.salom_ber("Shohruh")
