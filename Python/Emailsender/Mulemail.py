import re
import smtplib
from tkinter import EXCEPTION

print("\t\tTHIS IS EMAIL SENDING PYTHON PROGRAM YOU ARE WELCOME HERE !!!\n\n")

print("\tPLEASE CHOOSE YOUR PREFER OPTION :\n\t")
print("1:FOR SENDING EMAIL TO THE MULTIPLE USERS\t\t2:FOR SENDING EMAIL TO THE USER\n")
useroption = input("YOUR INPUT PLEASE :")
if useroption == "1":
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()

        server.login("checkemail299@gmail.com","poiglwjeoangqzxe")

        data = []
        E = "Y"
        while E =="Y":
            EMAIL_SEND_TO = input("ENTER EMAIL WHOM YOU WANT TO SEND :")

            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if(re.fullmatch(regex, EMAIL_SEND_TO)):
                #print("\tValid Email & EMAIL ADDED !!")
                data.append(EMAIL_SEND_TO)
                pass
            else:
                print("\tInvalid Email")

            INPUT = input("ADD MORE EMAIL (YorN):")
            if INPUT in "Yy":
                pass
            else:
                break
            

        #print(data)    
        f = open("emaildata.txt","w+")
        for i in data:
           # print(len(i))
            f.write(i+"\n")

        f.close()
        ndata = []
        f2 = open("emaildata.txt","r")        
        data = f2.readlines()
        #print(data)
        for i in data:
            i = i.strip("\n")
            ndata.append(i)
            #print(i)
            #print(len(i))

        #print(ndata)
        SUBJECT_OF_EMAIL = input("\n\tPLEASE ENTER YOUR EMAIL SUBJECT :")
        BODY_OF_EMAIL = input("\n\tENTER YOUR BODY :\n\t")

        msg = f'Subject : {SUBJECT_OF_EMAIL}\n\n{BODY_OF_EMAIL}'

        for i in ndata:
            server.sendmail("checkemail299@gmail.com" , i , msg )
            print("\tmail sent to "+i+" !")
    except EXCEPTION as error:
        print(error)
        print("PLEASE INSERT CORRECT CREDENTIALS !!")

elif useroption == "2":
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()

        server.login("checkemail299@gmail.com","poiglwjeoangqzxe")

        EMAIL_SEND_TO = input("ENTER EMAIL WHOM YOU WANT TO SEND :")

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, EMAIL_SEND_TO)):
            print("\tValid Email")
        else:
            print("\tInvalid Email")


        SUBJECT_OF_EMAIL = input("\n\tPLEASE ENTER YOUR EMAIL SUBJECT :")
        BODY_OF_EMAIL = input("\n\tENTER YOUR BODY :\n\t")

        msg = f'Subject : {SUBJECT_OF_EMAIL}\n\n{BODY_OF_EMAIL}'

        server.sendmail("checkemail299@gmail.com" , EMAIL_SEND_TO , msg )
        print("\n\tmail sent")

    except EXCEPTION as error:
        print(error)
        print("PLEASE INSERT CORRECT CREDENTIALS !!")
