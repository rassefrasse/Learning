sequence = int(input("Type length of sequence: "))

sequence1 = 0
sequence2 = 1


for i in range(1, sequence):
    i = sequence1 + sequence2
    sequence1 = sequence2
    sequence2 = i
    print(i)

