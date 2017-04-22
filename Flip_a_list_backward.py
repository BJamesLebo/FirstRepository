def traverse_back (Alist):
    newlist = []
    length = len(Alist)
    for i in range(0,len(Alist)):
        newlist.append(Alist[length-1])
        length = length - 1
    return newlist    
