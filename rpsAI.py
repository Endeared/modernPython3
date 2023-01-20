import random
computerChoices = ['rock', 'paper', 'scissors']

print("...rock...")
print("...paper...")
print("...scissors...")

count = 0

player1 = input("(Enter your choice): ")
computer = print("The computer plays: " + computerChoices[random.randint(0, len(computerChoices))])

print("SHOOT!")

if (player1.lower() == player2.lower()):
    print("TIE")
elif (player1.lower() == 'scissors' and player2.lower() == 'paper'):
    print("PLAYER 1 WINS")
elif (player1.lower() == 'scissors' and player2.lower() == 'rock'):
    print("PLAYER 2 WINS")
elif (player1.lower() == 'paper' and player2.lower() == 'rock'):
    print("PLAYER 1 WINS")
elif (player1.lower() == 'paper' and player2.lower() == 'scissors'):
    print("PLAYER 2 WINS")
elif (player1.lower() == 'rock' and player2.lower() == 'scissors'):
    print("PLAYER 1 WINS")
elif (player1.lower() == 'rock' and player2.lower() == 'paper'):
    print("PLAYER 2 WINS")
else:
    print("INVALID INPUT(S)!")