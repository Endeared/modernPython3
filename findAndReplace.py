def find_and_replace(file, find, replace):
    with open(file, 'r+', encoding='utf8') as toCheck:

        data = toCheck.read()
        
        newData = data.replace(find, replace)

        toCheck.seek(0)
        toCheck.write(newData)
        toCheck.truncate()