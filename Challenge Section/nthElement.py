def nth(list, shift):

    if shift < 0:
        list.reverse()
        return(list[abs(shift) - 1])
    elif shift == 0:
        return list[0]
    return list[shift]