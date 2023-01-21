def product(num1, num2):
    return(num1 * num2)

def return_day(num):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day = num - 1
    if day >= 0 and day <= 6:
        return(days[day])
    else:
        return None

def last_element(list):
    if len(list) > 0:
        return(list[len(list) - 1])
    else:
        return None