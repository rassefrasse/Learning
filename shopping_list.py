s_list = []

print("Good morning boss! Add items to the list and type #done when you're finished")

while True:
    add_list = input("What would you like to add to the list: ")
    s_list.append(add_list)

    if add_list == "#done":
        break

s_list.remove("#done")
print(s_list)

while True:
    remove_list = input("What have you taken from the list: ")
    s_list.remove(remove_list)
    print(s_list)

    if not s_list:
        break

print("Awesome, nice shopping!")