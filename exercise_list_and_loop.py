num = 0
final_num = 0.00
i = 'done'

while True:

    num = input("Enter a number: ")

    if num == i:
        break
    try:
        final_num = float(num) + final_num

    except:
        print("invalid input")
        continue





print(final_num)