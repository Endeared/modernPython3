print("...rock...")
print("...paper...")
print("...scissors...")

count = 15

player1 = input("(enter Player 1's choice): ")
while (count < 15):
    print("***NO CHEATING***")
    count = count + 1
player2 = input("(enter Player 2's choice): ")

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