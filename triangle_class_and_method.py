class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base
    
    def calculate_area(self):
        return self.height * self.base / 2


height = float(input("What's the height of the triangle? "))
base = float(input("What's the base of the triangle? "))

triangle = Triangle(height, base)
area = triangle.calculate_area()

print("The area of the triangle is: ", area)