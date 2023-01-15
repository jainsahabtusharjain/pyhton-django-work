import csv

data = []
def checkcsv():
    with open('mcqs.csv','r')as f:
        reed=csv.reader(f)
        t = True
        for row in reed:
            for rowele in row:
                if rowele[0] in "ABCD":
                    if rowele[1]=="]": 
                        t=False
                    else:
                        pass
                elif rowele[0] == "[":
                    if rowele[1] in "ABCD" and rowele[2] == "]":
                        data.append(rowele)
                        pass                            
                    else:
                        t=False    
    return t




















# def checkcsv():
#     with open('mcqs.csv','r')as f:
#         reading=csv.reader(f)
#         for row in reading:
#             print(row)
#             print()
#             for i in row:
#                 print(i)
#                 for e in i:
#                     #print(e)
#                     #print()
#                     #print("_____")
#                     #print()
#                     import pdb;pdb.set_trace()
#                     if  i[0] in "ABCD" :
#                         data.append(i)
#                     elif i[0]=="[":
#                         if i[1] in "ABCD" and i[2]=="]" :
#                             data.append(i)
#                             t=True
#                         #pass
#                     else:
#                         print("DScd")
#                         t=False
#                         break
#     return t,data
# q=checkcsv()                        

# if q==True:
#     print("hello")
# else:
#     print("Your csv file is not correct  l kl kl lk lk kl kk please insert correct data")

#import csv
# data=[]


# def checkcsv():
#     with open('mcqs.csv','r')as f:
#         reed=csv.reader(f)
#         t=True
#         flag=0
#         for row in reed:
#             if flag == 1:
#                 break
#             #print(row+["1"])
#             for rowele in row:
#                 #print(rowele+"2")
#                 #for ele in rowele:
#                     #print(len(rowele)-1)
#                     #print(ele)
#                     #import pdb;pdb.set_trace()
#                 if rowele[0] in "ABCD":
#                     if rowele[1]=="]": #for "A]:" this kind of error
#                         t=False
#                     else:
#                         data.append(rowele) #why to append ele if we don't check it
#                         pass
#                      #break
#                 # if rowele[0] in "ABCD":
#                 #     data.append(rowele)
#                 #     pass
#                 elif rowele[0] =="[":
#                     if rowele[1] in "ABCD" and rowele[2]=="]":
#                         data.append(rowele)
#                         pass                            
#                 else:
#                     t=False
#                     flag = 1
#                     break
            

#         #print(data)
#         return t            
# ch=checkcsv()
# print(ch)
# if ch==True:
#     print(data)
# else:
#     print('incorrect data')

