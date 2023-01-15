import csv
def options():
    with open ("mcq.csv",mode="w",newline="") as f:
        for i in range(1,11):
            w=csv.writer(f)
            a=input("A:")
            b=input("B:")
            c=input("C:")
            d=input("D:")
            w.writerow([a,b,c,d])
options()
