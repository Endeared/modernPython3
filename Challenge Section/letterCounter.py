def letter_counter(string, search):

    evalList = []
    string.lower()

    for char in string:
        evalList.append(char)

    count = evalList.count(search)
    return count