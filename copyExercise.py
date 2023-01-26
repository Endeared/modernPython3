def copy(file, newFile):
    with open(file, 'r') as firstFile, open(newFile, 'w+') as secondFile:
        for line in firstFile:
            secondFile.write(line)