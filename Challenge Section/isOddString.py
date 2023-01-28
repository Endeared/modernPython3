def is_odd_string(string):
    total = 0
    string.lower()

    for char in string:
        total += ord(char) - 96
    
    if total % 2 == 0:
        return False
    return True