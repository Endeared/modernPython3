def find_factors(number):
    divisible = []
    
    for i in range(1, number + 1):
        if number % i == 0:
            divisible.append(i)

    return divisible