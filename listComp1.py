list = ['Elie', 'Tim', 'Matt']
list2 = [1, 2, 3, 4, 5, 6]
answer = []
answer2 = []


for entry in list:
    answer.append(entry[0])

for num in list2:
    if num % 2 == 0:
        answer2.append(num)

print(answer)
print(answer2)