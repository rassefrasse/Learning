s_list = []

while True:
    add_list = input("Add a number to the list: ")

    if add_list == "stop":
        print("Stopping . . .")
        break

    try:
        s_list.append(float(add_list))
        print(s_list)

    except ValueError:
        print("That's not a number. . .")
        continue

count_number = float(input("What number should I count: "))

print(s_list.count(count_number))