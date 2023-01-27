def sum_pairs(list, target):
    first = 0
    index = 1

    for i in range(first, len(list)):
        for j in range (first + 1, len(list)):
            if list[i] + list[j] == target:
                toReturn = [list[i], list[j]]
                return toReturn
            j += 1
        i += 1

    return []
