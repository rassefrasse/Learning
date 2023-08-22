word_dictionary = {}

text_content = input("Input content: ").split()

for word in text_content:
    word = word.strip("!?,.").lower()

    if word:
        if word in word_dictionary:
            word_dictionary[word] += 1
        
        else:
            word_dictionary[word] = 1

print("Word frequency:", word_dictionary)