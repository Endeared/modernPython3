def valid_parentheses(string):
    count = 0
    i = 0

    while i < len(string):
        if (string[i] == ')'):
            count -= 1
        if (string[i] == '('):
            count += 1
        if (count < 0):
            return False
        i += 1
    
    return count == 0