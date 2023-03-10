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

def frequency(list, search_term):
    count = 0

    for value in list:
        if value == search_term:
            count += 1

    return count

def multiply_even_numbers(list):
    product = 1

    for number in list:
        if number % 2 == 0:
            product = product * number
    
    return product

def capitalize(string):
    capitalized = string[0].upper()
    newString = capitalized

    for char in string[1:]:
        newString += char

    return newString

def compact(list):
    new_list = []

    for value in list:
        if bool(value) == True:
            new_list.append(value)

    return(new_list)

def intersection(list1, list2):
    new_list = []

    for value in list1:
        if value in list2:
            new_list.append(value)

    return new_list

def isEven(num):
    return num % 2 == 0

def partition(list, isEven):
    truthy_list = []
    falsy_list = []


    for item in list:
        if (isEven(item) == True):
            truthy_list.append(item)
        elif (isEven(item) == False):
            falsy_list.append(item)
    
    return([truthy_list, falsy_list])