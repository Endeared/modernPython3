import csv

def update_users(searchFirst, searchLast, newFirst, newLast):
    count = 0

    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
    
    with open("users.csv", "w") as file:
        csv_writer = csv.writer(file)
        for row in rows:
            if row[0] == searchFirst and row[1] == searchLast:
                csv_writer.writerow([newFirst, newLast])
                count += 1
            else:
                csv_writer.writerow(row)
    
    return "Users updated: " + str(count) + "."