def vowel_count(string):
    vowels = ['a','e','i','o','u']
    letters = list(string)

    counts = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    for letter in letters:
        if letter.lower() in vowels:
            counts[letter.lower()] += 1

    for vowel in vowels:
        if counts[vowel] == 0:
            counts.pop(vowel, None)

    return counts
