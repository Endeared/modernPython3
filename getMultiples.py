def get_multiples(number=1, count=10):
    i = 1
    while i <= count:
        yield i * number
        i += 1
    raise StopIteration