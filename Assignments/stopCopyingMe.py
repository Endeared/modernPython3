msg = input("Say something!!\n")

lower = msg.lower()

while lower != "stop copying me":
    print(msg)
    msg = input()
    lower = msg.lower()