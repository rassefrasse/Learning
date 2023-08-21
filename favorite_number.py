num1 = float(input("What's your first favorite number? "))
num2 = float(input("What's your second favorite number? "))

sum_result = num1 + num2 
prod_result = num1 * num2
diff_result = num1 - num2
quot_result = num1 / num2

print("The sum of your two most favorite numbers is:", sum_result)
print("The product of your two most favorite numbers is:", prod_result)
print("The difference of your two most favorite numbers is:", diff_result)
print("The quotient of your two most favorite numbers is:", quot_result)

if sum_result >= 5:
    print("It's over 5!")

else:
    print("it's under 5!")

#The user inputs two numbers to determine the value of num1 and num2
#As the program wants to work with an integer and not a string, the float()function converts the string into a float number
#Then the 4 different variables determines the value of the num1 and num2 through different calculations.
#It prints out the calculations 4 times, and then I made an if statement just to practice.
#If the number is greater than 5 or >= than 5, it'll print "It's over 5!" and if it's anything else it'll say "It's under 5"!
#On second thought, an elif statement for == 5 would be a good indicator for when it's 5