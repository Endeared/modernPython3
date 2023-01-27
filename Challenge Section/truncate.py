def truncate(string, shorten):

    chars = list(string)
    newString = ""

    if shorten < 3:
        return "Truncation must be at least 3 characters."
    elif shorten > len(chars):
        return string

    for i in range(0, (shorten - 3)):
        newString += chars[i]

    return newString + "..."