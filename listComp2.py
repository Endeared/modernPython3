list1 = [1,2,3,4]
list2 = [3,4,5,6]
list3 = ['Elie', 'Tim', 'Matt']
answer = []
answer2 = []

for entry in list1:
    if entry in list2:
        answer.append(entry)

for entry in list3:
    new = entry[::-1]
    new2 = new.lower()
    answer2.append(new2)

print(answer)
print(answer2)

