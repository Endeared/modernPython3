import random
computerChoices = ['rock', 'paper', 'scissors']

print("...rock...")
print("...paper...")
print("...scissors...")

count = 0

player1 = input("(Enter your choice): ")
randomIndex = random.randint(0, len(computerChoices - 1))
computer = computerChoices[randomIndex]
print("The computer plays: " + computer)

print("SHOOT!")

if (player1.lower() == computer.lower()):
    print("TIE")
elif (player1.lower() == 'scissors' and computer.lower() == 'paper'):
    print("PLAYER 1 WINS")
elif (player1.lower() == 'scissors' and computer.lower() == 'rock'):
    print("PLAYER 2 WINS")
elif (player1.lower() == 'paper' and computer.lower() == 'rock'):
    print("PLAYER 1 WINS")
elif (player1.lower() == 'paper' and computer.lower() == 'scissors'):
    print("PLAYER 2 WINS")
elif (player1.lower() == 'rock' and computer.lower() == 'scissors'):
    print("PLAYER 1 WINS")
elif (player1.lower() == 'rock' and computer.lower() == 'paper'):
    print("PLAYER 2 WINS")
else:
    print("INVALID INPUT(S)!")