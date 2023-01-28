def sum_up_diagonals(mainList):
    
    i = 0
    sum = 0

    while i < len(mainList):
        sum += mainList[i][i]
        i += 1
    i = len(mainList) - 1
    j = 0

    while i >= 0:
        sum += mainList[i][j]
        i -= 1
        j += 1
    
    return sum