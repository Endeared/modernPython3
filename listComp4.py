vowels = ['a','e','i','o','u']
string = "amazing"

answer = [letter for letter in string if letter not in vowels]
print(answer)