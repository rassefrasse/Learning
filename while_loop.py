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

#this is the most complex one in my opinion, or well the most difficult one.
#Basically, it's a while loop. while True: input a number and then converts to a float
# if the number is over 0, it'll say keep going
#if it's under 0 it'll say go up
#if it's 0 it'll print "the number is 0, exiting the program" and then break the program or well exit it