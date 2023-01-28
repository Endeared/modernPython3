def reverse_vowels(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    saveVowels = []
    newString = ""
    count = 0

    for char in string:
        if char in vowels:
            saveVowels.append(char)

    saveVowels.reverse()

    for char in string:
        if char in vowels:
            newString += saveVowels[count]
            count += 1
        else:
            newString += char

    return newString
