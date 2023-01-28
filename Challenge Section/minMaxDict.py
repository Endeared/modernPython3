def min_max_key_in_dictionary(dictionary):

    highest = 0

    for item in dictionary:
        if item > highest:
            highest = item

    lowest = highest

    for item in dictionary:
        if item < lowest:
            lowest = item
    
    return [lowest, highest]