number_list = [] #Original list that will be sorted

while True:
    add_number = (input("Add a number: ")) #The user adds numbers

    if add_number == 'stop': #If the user inputs stop, then the loop breaks
        print("Stopping . . .")
        break

    try: 
        number_list.append(float(add_number)) #here the number is turned from a string, to a float and added to the list
        print(add_number, number_list) #also prints the number added and the current numbers in the list

    except ValueError: #since the number is converted into a float, if there's a letter then the program breaks
            print("not a number") #so instead it's printing out "that's not a number"
            continue #and thenn continues the program

    
even_numbers = [number for number in number_list if number % 2 == 0] #this is the new list, that takes the index of the number_list and only keeps the even numbers


print("Even numbers: ", even_numbers) #and then the even list is printed out