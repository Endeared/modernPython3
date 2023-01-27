def range_in_list(values, start=0, end=0):
    sum = 0
    
    if end == 0:
        end = len(values) - 1
    elif values == []:
        return 0

    while start <= end and start <= len(values) - 1:
        sum += values[start]
        start += 1
    
    return sum