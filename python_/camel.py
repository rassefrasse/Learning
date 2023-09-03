def CamelToe(string):
    camel = []
    for letter in string:
        camel.append(letter)

    upperCamel = [char.upper() if index % 2 == 0 else char for index, char in enumerate(camel) ]

    stringify = ''.join(upperCamel)
    print(stringify)
        
    

string = input("Give me a word/sentence: ")
CamelToe(string)