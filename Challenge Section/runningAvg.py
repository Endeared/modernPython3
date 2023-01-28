def running_average():
    running_average.sum = 0
    running_average.count = 0

    def getAvg(number):
        running_average.sum += number
        running_average.count += 1
        return running_average.sum / running_average.count
    
    return getAvg