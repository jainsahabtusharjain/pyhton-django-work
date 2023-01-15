import csv,base64

def main(password):
    sample_string = password
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string



passw = []
passl = []

def checkpass():
    encpass=[]
    with open('users.csv','r')as f:
        reade=csv.reader(f)
        for row in reade:
            #print(row[1::])
            for pas in row[1::]:
                #print(pas)
                encpass.append(pas)
        return encpass
# ch = checkpass()
# print(ch)



def decodedpass(ch):
    decpass = []
    for i in ch:
        base64_string =i
        base64_bytes = base64_string.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        decpass.append(sample_string)
    return decpass




































#ch = ["MTIz","MTIz","MjIw"]
# ch=checkpass()
# print(ch)
# cd = decodedpass(ch[1::])
# print(cd)       
#         return passl

# ch=checkpass()
# print(ch)
# print("--fnend--")


