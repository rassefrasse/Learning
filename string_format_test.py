print("Hey!\n\nWho\tAre\tYou?\n\n")
name = input("What's your name? ")
age = input("Awesome, how old are you? ")
origin = input("Where are you from? ")

response = ("Oh, awesome. Alright, hey {}. Must be nice being {} years old. I've always wanted to visit {}").format(name, age, origin)

print(response)