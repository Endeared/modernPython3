def remove_negatives(nums):
    copy = list(filter(lambda num: num > -1, nums))
    return copy