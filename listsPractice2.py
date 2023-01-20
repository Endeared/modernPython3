people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]

i = 0
while (i < len(people)):
    if people[i] == "Hanna":
        people[i] = "Hannah"
    elif people[i] == "Geoffrey":
        people[i] = "Jeffrey"
    elif people[i] == "aparna":
        people[i] = "Aparna"
    i += 1