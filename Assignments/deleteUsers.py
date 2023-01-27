import csv
 
def delete_users(firstName, lastName):
    count = 0

    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
 
    with open("users.csv", "w") as file:
        csv_writer = csv.writer(file)
        for row in rows:
            if row[0] == firstName and row[1] == lastName:
                count += 1
            else:
                csv_writer.writerow(row)
 
    return "Users deleted: " + str(count) + "."