def nth(list, shift):

    print(shift)
    if shift < 0:
        list.reverse()
        print(list)
        return(list[abs(shift) - 1])
    elif shift == 0:
        return list[0]
    return list[shift]