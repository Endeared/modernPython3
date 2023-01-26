listExample = [1,2,3,4,5,5,4,3,2,1,1,5,6]
# provide initial list of values
setExample = set(listExample)
# change list to set, which leaves only unique values
moreThanOne = []
# create empty list

for value in setExample:
    if listExample.count(value) > 2:
        moreThanOne.append(value)
# iterate through values in set, checking count of each value in original list
# if value appears more than twice in original list, append to empty list

print(moreThanOne)
# print new list of values that appear more than twice
