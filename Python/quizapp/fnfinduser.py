import csv

data=[]
def finduser(caseignore):
    with open('users.csv','r')as f:
        reader=csv.reader(f)
        for row in reader:
            data.append(row[0])
    if caseignore in data:
        return True
    else:
        print("! ! !")
        return False
    

def detail():
    return data
