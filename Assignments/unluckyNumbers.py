lower = input("Input your lower number:\n")
upper = input("Input your upper number:\n")
lower = int(lower)
upper = int(upper)


for num in range(lower, upper + 1):
    if num == 13 or num == 666:
        print(f'{num} is unlucky!')
    elif num % 2 == 0:
        print(f'{num} is even!')
    else:
        print(f'{num} is odd!')