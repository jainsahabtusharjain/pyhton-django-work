import csv,fnfinduser,stdiomask,encide


def storeNewuserdata():
    E = 'Y'
    data = fnfinduser.detail()
    header = ["Email","password"]
    f = open('users.csv','a+',newline='\n')
    writer = csv.writer(f)
    if header[0] not in data:
        writer.writerow(header)
    else:
        pass
    while E == 'Y' or E == 'y':
            Email = input("please ennter your email :")
            if Email in data:
                print("this email id already exist please try another email!")
                continue
            password = stdiomask.getpass(prompt="Please enter your password :",mask="*")  
            data1 = encide.main(password)
            data = [Email,data1]
            writer.writerow(data)
            E = input("you want to enter more user :")
            if E in "Nn":
                break
    f.close()    