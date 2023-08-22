dictionary = {}
time = list(range(0, 24))

while True:
    to_do = input("Input what to do: ")
    
    if to_do == "#stop":
        break

    task_time = int(input("Input a time (0-23): "))

    if task_time not in time:
        print("Invalid time. Input 0-23.")
        continue

    dictionary[to_do] = task_time

print(dictionary)
