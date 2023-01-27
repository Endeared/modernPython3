def includes(collection, value, startingIndex=None):

    if startingIndex == None:
        i = 0
    else:
        i = startingIndex

    if type(collection) == dict:
        if value in collection.values():
            return True
        else:
            return False
    
    while i < len(collection):
        if str(value) in str(collection[i]):
            return True
        i += 1

    return False