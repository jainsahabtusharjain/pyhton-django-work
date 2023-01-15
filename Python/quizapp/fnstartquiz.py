import csv,subprocess,time
from operator import index

def startquiz(UserEmail):
    questioncount = 0
    totalquestions = 0

    questiondata = []
    optiondata = []
    scount = 0

    with open('question.csv','r',newline='') as questionfile:
        questionreader = csv.reader(questionfile)
        for row in questionreader:
            questiondata.append(row)
        totalquestions = len(questiondata)
    
    with open('mcqs.csv','r',newline='') as mcqfile:
        mcqreader = csv.reader(mcqfile)
        for row in mcqreader:
            optiondata.append(row)

    while(questioncount < totalquestions):
        subprocess.call("cls" , shell=True)
        print("\n"+"welcome "+UserEmail+"\n")
        print("while entering multiple answers please use ',' inbetween"+"\n")
        print("\n"+ questiondata[questioncount][0])
        questionoptionarray = optiondata[questioncount]
        o_=''
        ans=""
        anslist=["a","A","b","B","c","C","d","D",","]
        for op in questionoptionarray:
            if "[" in op:
                i=questionoptionarray.index(op)         
                O=op
                o=list(O)
                for e in o:
                    if e=="[" or e=="]" in e:
                        o.remove(e)
                #print(o)
                o_="".join(o)
                questionoptionarray[i]=str(o_).replace(questionoptionarray[i],o_)
                ans=ans+questionoptionarray[i][0]
        #print(ans)
        print(questionoptionarray[0]+"\t"+questionoptionarray[1])
        print(questionoptionarray[2]+"\t"+questionoptionarray[3])
        useranswer = input("enter your answer = ")
        print("Your Input Is :",useranswer.upper())
        if len(useranswer)>1:
            if len(useranswer)<3:
                subprocess.call('cls',shell=True)
                print(questionoptionarray[0]+"\t"+questionoptionarray[1])
                print(questionoptionarray[2]+"\t"+questionoptionarray[3])
                useranswer = input("enter your answer = ")
                if len(useranswer)<3:
                    print("you are disqualified please try again")
                    time.sleep(1)
                    subprocess.call('cls && py login.py',shell=True)
                
            if useranswer[0] not in anslist or useranswer[2] not in anslist:
                    print("please enter valid input")
                    time.sleep(3)
                    subprocess.call('cls',shell=True)
                    print(questionoptionarray[0]+"\t"+questionoptionarray[1])
                    print(questionoptionarray[2]+"\t"+questionoptionarray[3])
                    useranswer = input("enter your answer = ")
                    if len(useranswer)>1:
                        if useranswer[0] in anslist or useranswer[2] in anslist:
                            print("Your Input Is :",useranswer.upper())
                            time.sleep(1)
                    else:
                        print("you are disqualified please try again")
                        time.sleep(1)
                        subprocess.call('cls && py login.py',shell=True)
        else:
            if useranswer[0] not in anslist :
                print("please enter valid input")
                time.sleep(1)
                subprocess.call('cls',shell=True)
                print(questionoptionarray[0]+"\t"+questionoptionarray[1])
                print(questionoptionarray[2]+"\t"+questionoptionarray[3])
                useranswer = input("enter your answer = ")
                if useranswer in anslist:
                    print("Your Input Is :",useranswer.upper())
                    time.sleep(1)
                else:
                    print("you are disqualified please try again")
                    time.sleep(1)
                    subprocess.call('cls && py login.py',shell=True)
        if len(ans) == (len(useranswer)-1):
            if len(useranswer)>1:
                if useranswer[0].upper() in ans and useranswer[2].upper() in ans:
                    fans = 0
                    uans = useranswer.split(",")
                    for uanswer in uans:
                        usr = uanswer.upper()
                        if usr in ans:
                            fans +=1
                    if fans == 2:
                        scount +=1
                        print (scount)
                        print()
                    else:
                        pass            
        elif len(ans) == len(useranswer) :
            if useranswer.upper() in ans:
                scount +=1
                print (scount)
            pass
        questioncount +=1
        time.sleep(3)
    print("your total score out of 10 is "+str(scount))    
    time.sleep(3)
    subprocess.call('cls' ,shell=True)
    print('\n'+'welcome'+UserEmail+'\n')