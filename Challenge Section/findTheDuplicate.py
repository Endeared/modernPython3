def find_the_duplicate(array):
    array.sort()

    for i in range(0, len(array) - 1):
        try:
            if array[i] == array[i + 1]:
                return array[i]
        except IndexError:
            pass
    
    return None