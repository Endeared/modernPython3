def next_prime():
    i = 2
    primes = set()

    while True:
        for num in primes:
            if i % num == 0:
                break
        else:
            primes.add(i)
            yield i
        i += i % 2 + 1