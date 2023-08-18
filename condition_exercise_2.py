while True:
    year_input = (input("Insert a year (or 'exit' to quit): "))

    if year_input.lower() == 'exit':
        print("Exiting the program")
        break

    year = int(year_input)

    try:
    
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("it's a leap year")


        else:
            print("it's not a leap year")

    except ValueError:
        if year_input.strip().isdigit():
            print("Year entered is not a leap year.")
        else:
            print("Invalid input. Please enter a valid year or 'exit'.")


