def generate_evens():
    list = []
    for num in range(1,50):
        if num % 2 == 0:
            list.append(num)
    return(list)

print(generate_evens())
