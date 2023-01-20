import random
num = -1

randomNum = random.randint(1, 10)

while num != randomNum:
    num = input("Guess a number between 1 and 10!\n")
    num = int(num)
    if num == randomNum:
        print("You guessed it! You won!")
        choice = input("Do you want to keep playing? (y/n)\n")
        if choice == "y":
            randomNum = random.randint(1, 10)
            num = -1
        else:
            break
    elif num != randomNum:
        print("Too low, try again!")
