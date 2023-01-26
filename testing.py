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



def count_nines(n):
    count = 1
    nines = 0
    
    if n > 10000000000000000:
        multiples = int(n/10000000000000000)
        remainder = n % 10000000000000000
        for i in range(1, multiples):
            nines += 5000000000000000
        
        if remainder > 565754:
            newMultiples = int(n/565754)
            newRemainder = n % 565754
            for i in range(1, newMultiples):
                nines += 275645
                
            while count <= newRemainder:
                if str(9) in str(count):
                    for char in str(count):
                        if char == str(9):
                            nines += 1
                count += 1
            return nines
        
        while count <= remainder:
            if str(9) in str(count):
                for char in str(count):
                    if char == str(9):
                        nines += 1
            count += 1
        return nines
    
    elif n > 100000000000:
        multiples = int(n/100000000000)
        remainder = n % 100000000000
        for i in range(1, multiples):
            nines += 48721702418

        while count <= remainder:
            if str(9) in str(count):
                for char in str(count):
                    if char == str(9):
                        nines += 1
            count += 1
        return nines
    
    elif n > 565754:
        multiples = int(n/565754)
        remainder = n % 565754
        for i in range(1, multiples):
            nines += 275645

        while count <= remainder:
            if str(9) in str(count):
                for char in str(count):
                    if char == str(9):
                        nines += 1
            count += 1
        return nines

    else:
        while count <= n:
            if str(9) in str(count):
                for char in str(count):
                    if char == str(9):
                        nines += 1
            count += 1
        return nines

print(count_nines(10000000000000000000))
