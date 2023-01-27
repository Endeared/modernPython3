def week():
    count = 0
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    while count < 7:
        yield weekdays[count]
        count += 1
    raise StopIteration