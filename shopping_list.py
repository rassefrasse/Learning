s_list = [] #created an empty list

print("Good morning boss! Add items to the list and type #done when you're finished") #happy greeting

while True:
    add_list = input("What would you like to add to the list: ") #an input that lets the user add things to the list
    s_list.append(add_list) #sends the items to the list with the .append method

    if add_list == "#done": #if the user types #done it breaks the while loop
        break

s_list.remove("#done") #removves the #done from the list, so that it doesn't clog it up
print(s_list) #prints the finished list

while True:
    remove_list = input("What have you taken from the list: ") #same principle but a new variable
    s_list.remove(remove_list) #removes items from the list with the .remove method
    print(s_list) #prints out the list each time something is removed so the user gets an updated list

    if not s_list: #if there's nothing in the list the loop breaks
        break

print("Awesome, nice shopping!") #happy gd bye