def titleize(string):
    words = string.split(" ")
    newList = []

    for word in words:
        new = word[:1].upper() + word[1:]
        newList.append(new)

    newString = " ".join(newList)
    return newString