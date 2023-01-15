import csv


def showallusers():
    with open('users.csv','r',newline='')as f:
        read=csv.reader(f)
        for row in read:
            print(row)