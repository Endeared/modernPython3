import csv

def print_users():
    with open("users.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row['First Name'] + " " + row['Last Name'])