listExample = [1,8,23,24,33,34,54,75]
highest = 0

for num in listExample:
    if num > highest and num < 60:
        highest = num

print(highest)



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
