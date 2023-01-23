def sum_even_values(*args):
    sum = 0
    for num in args:
        if num % 2 == 0:
            sum += num
    return sum