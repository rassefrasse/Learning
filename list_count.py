s_list = [] #Empty list

while True:
    add_list = input("Add a number to the list: ") #User inputs number into list

    if add_list == "stop": #Stops input
        print("Stopping . . .")
        break

    try:
        s_list.append(float(add_list)) #Adds to the list and converts to float
        print(s_list)

    except ValueError:
        print("That's not a number. . .") #Continues the program
        continue

count_number = float(input("What number should I count: ")) #Lets the user input what number they should count, turns into float since we're targeting floats

print(s_list.count(count_number)) #outputs the count_number which is the stored user input, and counts how many times it appears