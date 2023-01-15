import requests
import json
from datetime import date
import csv
import time

result = requests.get("https://fakestoreapi.com/products")
data = result.text
parse_json = json.loads(data)
today = date.today()

cat_data = []
for i in parse_json:
    if i['category'] not in cat_data:
        cat_data.append(i['category'])
    else:
        pass
print("This is the categories from which you can get data :-")


count = 0
ndict = {}
for i in cat_data:
    count +=1
    ndict[count] = i
    print("\t"+str(count)+" "+i)
print()


categ = input("Please enter your corresponding category number for which you want data : ")
if int(categ) >  count:
    print("Please choose correct category")
    time.sleep(2)
    import subprocess;subprocess.call("cls && py newapi.py", shell=True)
    # import pdb;pdb.set_trace()
else:
    category = (ndict[int(categ)])
    if category not in cat_data:
        print("Please enter correct category")
        category = input("enter your category for which you want data : ")
    for i in parse_json:
        if i['category'] == category:
            f_name = (f"{category}_"+str(today))
            with open(f_name+'.csv',"w")as f:
                writ = csv.DictWriter(f, fieldnames= ['id','title', 'price', 'description','category','image','rate','count'])
                writ.writeheader()
            for i in parse_json:
                row = []
                if i['category'] == category:
                    row.append(i['id'])
                    row.append(i['title'])
                    row.append(i['price'])
                    row.append(i['description']) 
                    row.append(i['category'])
                    row.append(i['image'])
                    row.append(i['rating']['rate'])
                    row.append(i['rating']['count'])
                    with open(f_name+'.csv','a+') as f1:
                        writ = csv.writer(f1)
                        writ.writerow(row)
            break
    print(f"\nYour data is sucessfully saved for {category}!!")