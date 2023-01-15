import re,subprocess
print("\t\tTHIS IS EMAIL SENDING PYTHON PROGRAM YOU ARE WELCOME HERE !!!\n\n")
print("\tPLEASE CHOOSE YOUR PREFER OPTION :\n\t")
print("1:FOR SENDING EMAIL TO THE MULTIPLE USERS\t\t2:FOR SENDING EMAIL TO THE USER\n")
useroption = input("YOUR INPUT PLEASE :")
if useroption == "1":
    E = "Y"
    stdata = []
    while E == "Y":
        data = input("PLEASE ENTER EMAIL ID :")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, data)):
            #print("\tValid Email")
            pass
        else:
            print("\tInvalid Email")
            import time;time.sleep(1)
            subprocess.call("cls && py extra.py",shell=True)
        stdata.append(data)
        In = input("ENTER MORE USER EMAIL (Y/N):")
        if In in "Yy":
            pass
        else:
            break
    print(stdata)
    with open("emaildata.txt", 'w+') as f:
        #import pdb;pdb.set_trace()
        f.writelines(stdata)
        new = f.read()
        for i in new:
            print(data)