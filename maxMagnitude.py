def max_magnitude(nums):
    furthest = 0
    for num in nums:
        if abs(num) > furthest:
            furthest = abs(num)

    return furthest