class Calculator():            #name of the class
    def __init__(self, a, b):  #initializing the variables that will be used
        self.a = a
        self.b = b

    def add(self):              #creating the METHOD .add
        return self.a + self.b  #anything used in the function, not the answers
                                #the method does a + b
    def subtract(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b


i = Calculator(200, 20)         # and here we say that i equals to, in the class "Calculator", a = 200, b = 20

print(Calculator.add(i))        # and then we print out the method which is in this case addition, 200 + 20
print(i.add())