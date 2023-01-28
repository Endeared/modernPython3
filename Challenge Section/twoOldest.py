def two_oldest_ages(li):
    li.sort()
    return [li[len(li) - 2], li[len(li) - 1]]