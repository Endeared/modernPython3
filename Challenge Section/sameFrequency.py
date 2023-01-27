def same_frequency(numberOne, numberTwo):
    numsOne = list(str(numberOne))
    numsTwo = list(str(numberTwo))
    numsOne.sort()
    numsTwo.sort()

    if numsOne == numsTwo:
        return True
    
    return False