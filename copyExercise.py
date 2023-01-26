def copy_and_reverse(file, newFile):
    with open(file, 'r') as firstFile, open(newFile, 'w+') as secondFile:
        data = firstFile.read()
        dataReverse = data[::-1]
        secondFile.write(dataReverse)