class Rectangle:

   

    def __init__(self, height, width):
        self.height = height
        self.width = width
        return
    
    
    def calculate_area(self):
        return self.height * self.width



height = float(input("What's the height of the rectangle? "))
width = float(input("What's the width of the rectangle? "))

rectangle = Rectangle(height, width)
area = rectangle.calculate_area()

print(area)
