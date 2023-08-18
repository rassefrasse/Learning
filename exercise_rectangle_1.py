def calculation(w, h):
    return h * w
    
while True:
    height = float(input("What is the height of the rectangle?(in cm) "))
    width = float(input("What is the width of the rectangle?(in cm) "))

    result = calculation(height, width)

    print("The area of your rectangle is(in cm): ", result)

