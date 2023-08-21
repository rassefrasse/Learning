glosor = { #dictionary with swedish vs french dictionary
    "tack":"merci",
    "hej":"bonjour",
    "god kväll":"bonsoir",
    "taxi":"taxi",
    "hur mår du":"ca va"
}

for svenskt_ord in glosor: #for each svenskt_ord(temporary variable) in the dictionary "glosor"
    svar = glosor[svenskt_ord] #created a new variable and assigned it with the value of each svenskt_ord in the dictionary

    fraga = input("Vad är " + svenskt_ord + " på franska: ").lower() #input what is the swedish word in french, lower case it all
    
    if fraga == svar: #if the fraga/variable is assigned to the french word, print and continue
        print("snyggt!!")
    
    elif fraga == "afk": #just a quit statement
        break

    else: #if the key isn't the same, print that it's wrong
        print("FEL")

print("grattis du är smartare än en 8 åring!")

