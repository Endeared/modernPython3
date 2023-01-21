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

def number_compare(num1, num2):
    if num1 > num2:
        return("First is greater")
    elif num2 > num1:
        return("Second is greater")
    else:
        return("Numbers are equal")

def single_letter_count(string, letter):
    string = string.lower()
    letter = letter.lower()
    count = 0
    for char in string:
        if char == letter:
            count += 1
    if count == 0:
        return(0)
    else:
        return(count)

def multiple_letter_count(string):
    string = string.lower()
    chars = []

    for char in string:
        chars.append(char)
    
    counts = dict.fromkeys(chars, 0)

    for char in string:
        counts[char] = counts[char] + 1

    return(counts)

def list_manipulation(list, command, location, value=None):
    if command.lower() == "remove" and location.lower() == "end":
        return(list.pop(len(list) - 1))
    elif command.lower() == "remove" and location.lower() == "beginning":
        return(list.pop(0))
    elif command.lower() == "add" and location.lower() == "beginning":
        list.insert(0, value)
        return list
    elif command.lower() == "add" and location.lower() == "end":
        list.append(value)
        return list

def is_palindrome(string):
    newString = ""
    for char in reversed(string):
        if char != " ":
            newString += char
    
    if newString.lower() == string.lower():
        return True
    
    return False