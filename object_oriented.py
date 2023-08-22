class Dog:

    def __init__(self, name):
        self.name = name
        print(name)

    def add(self, x):
        return x + 1

    def bark(self):
        print("bark")

d = Dog("Rasmus")
d2 = Dog("Thierry")
