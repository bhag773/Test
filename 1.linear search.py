nlist = [1,3,4,5,63,65,2,56,88,22,11,78] # unordered list of numbers
search_term = 11 #  The number which is being compared
found = False

for x in range(len(nlist)): # x is the index of the list
    if search_term == nlist[x]: #nlist x correspponds to the value of the index x in the list
        found = True

if found:
    print("Found Data item")
else:
    print("Not found data item")
