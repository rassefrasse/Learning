def Add():
    a1 = float(input("Enter a number: "))
    a2 = float(input("Enter a second number: "))
    a3 = a1 + a2
    return a3

def Subtract():
    s1 = float(input("Enter a number: "))
    s2 = float(input("Enter a second number: "))

    s3 = s1 - s2
    return s3

def Multiply():
    m1 = float(input("Enter a number: "))
    m2 = float(input("Enter a second number: "))
    m3 = m1 * m2 
    return m3

def Divide():
    d1 = float(input("Enter a number: "))
    d2 = float(input("Enter a second number: "))
    d3 = d1 / d2
    return d3

while True:
    what_to_do = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n\nWhere To Go:")
    try: 
        what_to_do = int(what_to_do)

        if what_to_do == 1:
            print("Commensing Addition . . .")
            Result = Add()
            print("Result: ", Result)
        elif what_to_do == 2:
            print("Commensing Subtraction . . .")
            Result = Subtract()
            print("Result: ", Result)
        elif what_to_do == 3:
            print("Commensing Multiplication . . .")
            Result = Multiply()
            print("Result: ", Result)
        elif what_to_do == 4:
            print("Commensing Division . . .")
            Result = Divide()
            print("Result: ", Result)
        elif what_to_do == "#done":
            break
        else:
            print("Invalid input. Please enter a number (1-4) or type #done to exit.")
            continue

    except ValueError:
        print("Invalid input. Please enter a number (1-4) or type #done to exit.")
        continue