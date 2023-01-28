def find_greater_numbers(li):
    count = 0
    i = 0
    j = 1

    while i < len(li):
        while j < len(li):
            if li[j] > li[i]:
                count += 1
            j += 1
        j = i + 1
        i += 1
    return count