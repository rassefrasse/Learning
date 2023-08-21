text_content = input("Input content: ") #inputs the text
words = text_content.split() #splits the text into different parts
word_frequency = {} #empty dictionary where the text will be stored

for word in words: #for each word in the words variable up there^
    word = word.strip(".,?!-").lower() #remove all dots, commas, question marks and exclamation marks and lower the cases

    if word in word_frequency: #if word in the word_frequency dictionary exists, add +1 to its assigned value
            word_frequency[word] += 1
    else: #assigns the value 1 to all words in the dictionary
            word_frequency[word] = 1

most_common_keywords = sorted(word_frequency, key=word_frequency.get, reverse=True)[:5]
#^the most common keywords = sorted word_frequency in reverse, get the key in the word_frequency and then rank the top 5

print("Most common words: ", len(word_frequency))
print("Word frequency: ", word_frequency)
print("Most common words: ", most_common_keywords)
