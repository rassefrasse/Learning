starting_price = int(input("Starting price: "))
price_rise = int(input("How much will the item rise in price: "))
amount_to_buy = int(input("How many will you buy: "))

result = 0

for i in range(1, amount_to_buy + 1):   
    
    if i % 5 == 0:
        result += starting_price

    starting_price += price_rise
    
print(result)   