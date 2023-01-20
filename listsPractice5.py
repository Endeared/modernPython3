instructors = []
toAdd = ['Colt', 'Blue', 'Lisa']
i = 0


while (i < len(toAdd)):
    instructors.append(toAdd[i])
    i += 1

instructors.pop(len(instructors) - 1)
instructors.pop(0)
instructors.insert(0, "Done")

print(instructors)