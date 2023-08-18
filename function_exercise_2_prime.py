def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
    
num = int(input("Enter number: "))
if is_prime(num):
    print("it's a prime number")
else:
    print("it's not a prime number")
