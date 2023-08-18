while True:
    number = float(input("Enter a number (0 to quit):"))

    if number > 0:
        print("Keep going")
    elif number < 0:
        print("go up")
    else:
        print("the number is 0")

    if number == 0:
        print("exiting the program")
        break