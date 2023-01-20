from random import randint

number = 0
i = 0


number = randint(1,10)
while number != 5:
    i += 1
    print(i)
    print(number)
    number = randint(1,10)