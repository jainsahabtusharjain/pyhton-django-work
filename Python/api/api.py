import requests
import json
import csv

result = requests.get('https://fakestoreapi.com/products')

data = result.text

parse_json = json.loads(data)

# print(parse_json)

# for i in parse_json:
#     s = i.items()
#     for j in s:
#         print(j)

with open('newdata.csv','w')as f:
    writ = csv.DictWriter(f, fieldnames= ['id','title', 'price', 'description','category','image','rate','count'])
    writ.writeheader()

for i in parse_json:
    row = []
    row.append(i['id'])
    row.append(i['title'])
    row.append(i['price'])
    row.append(i['description']) 
    row.append(i['category'])
    row.append(i['image'])
    row.append(i['rating']['rate'])
    row.append(i['rating']['count'])
    with open('newdata.csv','a+') as f1:
        writ = csv.writer(f1)
        writ.writerow(row)