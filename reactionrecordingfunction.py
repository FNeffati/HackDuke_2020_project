

import csv


def fun(): 
    filename = input("What is the name of the file you would like to add this information to? ")
    name = input("Enter your name: ")
    days = input("How many days ago did you recieve the vaccine? ")
    cough = input("What is the adverse reaction that you experienced? ")

    newInfo = [name, days, cough]

    new_rows = []

    with open(filename) as file:
        reader = csv.reader(file) 
        for row in reader:
            print(row)
            new_rows.append(row)
        
        new_rows.append(newInfo);

    writef = open(filename, 'w', newline='')
    writer = csv.writer(writef)
    writer.writerows(new_rows)

    file.close()
    writef.close()
