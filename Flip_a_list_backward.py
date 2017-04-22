def traverse_back (Alist):
    newlist = []
    lengthboy = len(Alist)
    for i in range(0,len(Alist)):
        newlist.append(Alist[lengthboy-1])
        lengthboy = lengthboy - 1
    return newlist    
