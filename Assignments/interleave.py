def interleave(string1, string2):
    string = ''
    zipped = zip(string1, string2)
    for set in zipped:
        for char in set:
            string += char
    return string
