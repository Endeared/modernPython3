def extract_full_name(names):
    nameList = []
    for person in names:
        name = person['first'] + " " + person['last']
        nameList.append(name)
    return nameList