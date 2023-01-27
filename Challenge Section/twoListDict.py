def two_list_dictionary(listOne, listTwo):
    dict = {}
    i = 0

    for value in listOne:
        try:
            dict[value] = listTwo[i]
        except IndexError:
            dict[value] = None
        i += 1

    return dict