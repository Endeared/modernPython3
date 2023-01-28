def three_odd_numbers(li):
    i = 0

    while i < len(li) - 2:
        if (li[i] + li[i + 1] + li[i + 2]) % 2 != 0:
            return True
        i += 1

    return False