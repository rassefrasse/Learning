starting_price = int(input("Starting price: ")) #all of these inputs are self explanatory
price_rise = int(input("How much will the item rise in price: "))
amount_to_buy = int(input("How many will you buy: "))

result = 0 #set default value to the result

for i in range(1, amount_to_buy + 1): #for loop, for each i in range 1, to amount_to_buy +1 obviously
    
    if i % 5 == 0: #per each 5, add the starting price + the result to change the value of result
        result += starting_price

    starting_price += price_rise #the starting price ahtever it be + the rise in price
    
print(result)   