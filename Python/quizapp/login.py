import time,subprocess,fnfinduser,fnshowalluser,fnstorenewuser,fnstudentoptions,fnstartquiz,stdiomask,encide,checkcsv

ch=checkcsv.checkcsv()
print(ch)
if ch:
    print("your csv file is correct")
    subprocess.call("cls" , shell=True)
else:
    print('incorrect data please insert correct csv data')
    time.sleep(2.5)
    exit()
subprocess.call("cls" , shell=True)

passw = []
nstr = []
ste = ''

email = input('enter your email address = ')
caseignore = email.lower()
username = fnfinduser.finduser(caseignore)
if username:
    password=stdiomask.getpass(prompt="enter your password :", mask="*") 
    ch=encide.checkpass()
    #cd=encide.decodedpass(ch)
    cd = encide.decodedpass(ch[1::])
    #print(cd)
    if password in cd:
        print("congratulation !!")
    else:
        print("Please enter correct password ")
        time.sleep(6)
        subprocess.call("cls && py login.py" , shell=True)        
else:
    pass
if username == True:
    print("\nwelcome"+"\t"+email+'\n') 
    while(email):
        userchoice = fnstudentoptions.appoptions()
        subprocess.call('cls',shell=True)
        print("\nwelcome"+ email +"\n")
        if (userchoice == 1):
            fnshowalluser.showallusers()
        if (userchoice == 2):
            fnstartquiz.startquiz(email)
        elif (userchoice == 3):
            email = ' '
            subprocess.call("py login.py" , shell=True)
        elif (userchoice == 4): 
            email = ''
            subprocess.call("cls" , shell=True)
        elif (userchoice ==5):
            ch=checkcsv.checkcsv()
            print(ch)
            if ch:
                print("your csv file is correct")
                time.sleep(2.5)
                subprocess.call("cls && py login.py" , shell=True)
            else:
                print('incorrect data')
else:
    print("This email id is not registered please registered this email thanku! ")
    fnstorenewuser.storeNewuserdata()
    subprocess.call("cls && py login.py" , shell=True)