text_content = input("Input content: ")
words = text_content.split()
word_frequency = {}

for word in words:
    word = word.strip(".,?!-").lower()

    if word:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

most_common_keywords = sorted(word_frequency, key=word_frequency.get, reverse=True)[:5]

print("Most common words: ", len(word_frequency))
print("Word frequency: ", word_frequency)
print("Most common words: ", most_common_keywords)
