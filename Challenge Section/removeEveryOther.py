def remove_every_other(list):
    index = 0
    newList = []

    while index < len(list):
        newList.append(list[index])
        index += 2

    return newList