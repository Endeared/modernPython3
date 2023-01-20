import random
computerChoices = ['rock', 'paper', 'scissors']

print("...rock...")
print("...paper...")
print("...scissors...")

count = 0

player1 = input("(Enter your choice): ")
randomIndex = random.randint(0, (len(computerChoices) - 1))
computer = computerChoices[randomIndex]
print("The computer plays: " + computer)

print("SHOOT!")

if (player1.lower() == computer.lower()):
    print("TIE!")
elif (player1.lower() == 'scissors' and computer.lower() == 'paper'):
    print("YOU WIN!")
elif (player1.lower() == 'scissors' and computer.lower() == 'rock'):
    print("COMPUTER WINS!")
elif (player1.lower() == 'paper' and computer.lower() == 'rock'):
    print("YOU WIN!")
elif (player1.lower() == 'paper' and computer.lower() == 'scissors'):
    print("COMPUTER WINS!")
elif (player1.lower() == 'rock' and computer.lower() == 'scissors'):
    print("YOU WIN!")
elif (player1.lower() == 'rock' and computer.lower() == 'paper'):
    print("COMPUTER WINS!")
else:
    print("INVALID INPUT(S)!")