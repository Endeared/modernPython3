def triple_and_filter(nums):
    filtered = filter(lambda num: num % 4 == 0, nums)
    newList = list(map(lambda num: num * 3, filtered))
    return newList