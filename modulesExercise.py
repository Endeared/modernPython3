import keyword

def contains_keyword(*args):
    for word in args:
        if keyword.iskeyword(word) == True:
            return True
    return False