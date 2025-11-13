nlist = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29] # ordered list of numbers

search_term = 25 # #  The number which is being compared
found = False
first = 0 # first index of a list is 0 therefore first is set to 0
last = len(nlist) -1 # because the first index is 0 the last index is 1 less than the original length of the list

while found == False and last >= first: 
    mid = (first + last) // 2 #mid is the middle index of the list

    if search_term == nlist[mid]:
        found = True
        break

    if search_term > nlist[mid]:
        first = mid + 1 # list is halved to the second half 
    else:
        last = mid -1# list is halved to the first half

if found:
    print("Found data item")
else:
    print("Not found data item")
