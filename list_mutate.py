def remove_dups(L1, L2):
    for e in L1: 
        if e in L2: 
            L1.remove(e) # this will change length of L1, but internal counter has not been updated; counter will be at first index, but old first index is now 0th index in array

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)

