def statistics(file):
    with open(file, encoding='utf8') as toCheck:

        data = toCheck.read()
        words = data.split()
        characters = list(data)
        lines = toCheck.readlines()

        length = len(lines)
        numOfWords = len(words)
        numOfChars = len(characters)

        return {
            "lines": length,
            "words": numOfWords,
            "characters": numOfChars
        }

print(statistics("story.txt"))
        