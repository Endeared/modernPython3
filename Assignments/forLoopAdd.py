x = 0

lowerRange = int(input("Input your low number!\n"))
upperRange = int(input("Input your high number!\n"))

for i in range(lowerRange, upperRange + 1):
    if i % 2 != 0:
        x = x + i

print(f'The sum of all ODD numbers from {lowerRange} to {upperRange} is {x}!')