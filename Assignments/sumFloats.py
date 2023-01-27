def sum_floats(*args):
    sum = 0
    for num in args:
        if type(num) == float:
            sum += num
    return sum