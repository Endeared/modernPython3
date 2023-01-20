import random
computerChoices = ['rock', 'paper', 'scissors']

print("...rock...")
print("...paper...")
print("...scissors...")

count = 0
playerWins = 0
computerWins = 0


while True:
    player1 = input("(Enter your choice): ")
    randomIndex = random.randint(0, (len(computerChoices) - 1))
    computer = computerChoices[randomIndex]
    print("The computer plays: " + computer)

    print("SHOOT!")

    if (player1.lower() == computer.lower()):
        print("TIE!")
        print(f'Player score: {playerWins} | Computer score: {computerWins}')
    elif (player1.lower() == 'scissors' and computer.lower() == 'paper'):
        print("YOU WIN!")
        playerWins += 1
        print(f'Player score: {playerWins} | Computer score: {computerWins}')
    elif (player1.lower() == 'scissors' and computer.lower() == 'rock'):
        print("COMPUTER WINS!")
        computerWins += 1
        print(f'Player score: {playerWins} | Computer score: {computerWins}')
    elif (player1.lower() == 'paper' and computer.lower() == 'rock'):
        print("YOU WIN!")
        playerWins += 1
        print(f'Player score: {playerWins} | Computer score: {computerWins}')
    elif (player1.lower() == 'paper' and computer.lower() == 'scissors'):
        print("COMPUTER WINS!")
        computerWins += 1
        print(f'Player score: {playerWins} | Computer score: {computerWins}')
    elif (player1.lower() == 'rock' and computer.lower() == 'scissors'):
        print("YOU WIN!")
        playerWins += 1
        print(f'Player score: {playerWins} | Computer score: {computerWins}')
    elif (player1.lower() == 'rock' and computer.lower() == 'paper'):
        print("COMPUTER WINS!")
        computerWins += 1
        print(f'Player score: {playerWins} | Computer score: {computerWins}')
    else:
        print("INVALID INPUT(S)!")