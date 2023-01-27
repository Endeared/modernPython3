import csv

def add_user(firstName, lastName):
    with open("users.csv", "a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([firstName, lastName])
        

add_user("test", "name")
