def averageList(myList):
    avg = 0
    for elt in myList:
        avg += elt
    if len(myList) == 0:
        return None;
    else:
        avg = avg / len(myList)
        return avg
