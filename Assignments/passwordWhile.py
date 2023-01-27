msg = input("Input a password:\n")
inputPw = input("Input your password to login:\n")

while msg != inputPw:
    print("Incorrect password.")
    inputPw = input("Try again:\n")
print("SUCCESS!")
