smallest = None 
print("Before:", smallest) #dunno why, but just prints None ig
for itervar in [3, 41, 12, 9, 74, 15]: #should've made a seperate empty list that people can input ints
    if smallest is None or itervar < smallest: #if smallest has no value or if itervar is smaller than smallest...
        smallest = itervar #then assign smallest the value of itervar
        
print("Loop:", itervar, smallest)
print("Smallest:", smallest)