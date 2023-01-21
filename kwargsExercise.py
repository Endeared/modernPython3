def combine_words(string, **kwargs):
    for type, add in kwargs.items():
        if "prefix" in kwargs:
            return(add + string)
        elif "suffix" in kwargs:
            return(string + add)
        else:
            return(string)

print(combine_words("child"))