from logging import exception
import re
import smtplib
#from tkinter import EXCEPTION

print("\t\tTHIS IS EMAIL SENDING PYTHON PROGRAM YOU ARE WELCOME HERE !!!\n\n")

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

except exception as error:
    print(error)
    print("PLEASE INSERT CORRECT CREDENTIALS !!")

