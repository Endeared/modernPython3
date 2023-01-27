def combine_words(string, **kwargs):
    for type, add in kwargs.items():
        if type == "prefix":
            return(add + string)
        elif type == "suffix":
            return(string + add)
    return(string)