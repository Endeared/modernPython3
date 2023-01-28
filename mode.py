def mode(li):
    tup = tuple(li)
    count = 0
    value = None

    for value in tup:
        if li.count(value) > count:
            count = li.count(value)
            value = li.count(value)
    
    return value