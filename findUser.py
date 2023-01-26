import csv

def find_user(firstName, lastName):
    with open('users.csv') as file:
        csv_reader = csv.reader(file)
        for (i, row) in enumerate(csv_reader):
            if row[0] == firstName and row[1] == lastName:
                return i
        return(firstName + " " + lastName + " not found.")