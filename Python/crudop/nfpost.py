import psycopg2

connector = psycopg2.connect(
host = "localhost",
user = "postgres",
password = "tushar123",
database = "learn",
port = 5432
)
database = "learn"
cursorobject = connector.cursor()
print("\t\tYour current Database is :"+database+"!"+" Of postgresql\n\n") 
cursorobject.execute("CREATE TABLE IF NOT EXISTS users(FirstName varchar(50) unique not null,LastName TEXT not null,City TEXT not null)")
connector.commit()


def useroption():
    print("Please choose What You Want to Do :"+"\n")
    print("\t1:CREATE\t2:READ\t\t3:UPDATE\t4:DELETE\t5:Quit\n")
    In = input("Your Choice :")

    if In == "1":
        E = "Y"
        while E in "Yy":
            sql = "INSERT INTO users (FirstName,LastName,City) VALUES(%s, %s, %s)"
            val = (
                input("FirstName :"),
                input("LastName :"),
                input("City :")
                )
            try:
                cursorobject.execute(sql, val)
                connector.commit()
                E = input("WANT TO ENTER MORE USER :")
                if E in "Nn":
                    break
            except Exception as error:
                print(error)
        inpt = input("PRESS ANY KEY TO CONTINUE :")
        if inpt != "":
            pass
        import subprocess;subprocess.call("cls",shell=True)
        useroption()
        
    elif In == "2":
        sql = "SELECT * FROM users"
        try:
            cursorobject.execute(sql)
            myresult = cursorobject.fetchall()
            if myresult == []:
                print("PLEASE INSERT DATA FIRST THANKU !")
                import time;time.sleep(2)
                import subprocess;subprocess.call("cls && py nfpost.py",shell=True)
            else:
                for x in myresult:
                    print(x)
            connector.commit()
        except Exception as error:
            print(error)
        inpt = input("PRESS ANY KEY TO CONTINUE :")
        if inpt != "":
            pass
        import subprocess;subprocess.call("cls",shell=True)
        useroption()

    elif In == "3":
        print("     WHAT YOU WANT TO UPDATE     ","\n\t1:FirstName\n\t2:LastName\n\t3:City\n")
        uso = input("YOUR INPUT :")

        if uso == "1":
            S = "Y"
            while S in "Yy":
                fname = input("INSERT YOUR OLD FIRST NAME :")
                updatename = input("INSERT YOUR NEW FIRST NAME :")
                sql = "update users set FirstName=%s where FirstName=%s"
                try:
                    cursorobject.execute(sql,(updatename,fname))
                    print("Updated Sucessfuly !")
                    connector.commit()
                    S = input("WANT TO UPDATE MORE NAME :")
                    if S in "Nn":
                        break
                except Exception as error:
                    print(error)
    
        elif uso == "2":
            S = "Y"
            while S in "Yy":
                lname = input("INSERT YOUR OLD LAST NAME :")
                updatelname = input("INSERT YOUR NEW LAST NAME :")
                sql = "update users set LastName=%s where LastName=%s"
                try:
                    cursorobject.execute(sql,(updatelname,lname))
                    print("Updated Sucessfuly !")
                    connector.commit()
                    S = input("WANT TO UPDATE MORE NAME :")
                    if S in "Nn":
                        break
                except Exception as error:
                    print(error)

        elif uso == "3":
            S = "Y"
            while S in "Yy":
                cityname = input("INSERT YOUR OLD CITY NAME :")
                updatedcity = input("INSERT YOUR NEW CITY NAME :")
                sql = "update users set City=%s where City=%s"
                try:
                    cursorobject.execute(sql,(updatedcity,cityname))
                    print("Updated Sucessfuly !")
                    connector.commit()
                    S = input("WANT TO UPDATE MORE NAME :")
                    if S in "Nn":
                            break
                except Exception as error:
                    print(error)
        inpt = input("PRESS ANY KEY TO CONTINUE :")
        if inpt != "":
            pass
        import subprocess;subprocess.call("cls",shell=True)
        useroption()

    elif In == "4":
        S = "Y"
        while S in "Yy":
            delname =input("DELETE THE ROW OF:")
            sql = "DELETE FROM users WHERE FirstName =%s"
            try:
                cursorobject.execute(sql,(delname,))
                connector.commit()
                S = input("WANT TO DELETE MORE NAME :")
                if S in "Nn":
                    break
            except Exception as error:
                print(error)
        inpt = input("PRESS ANY KEY TO CONTINUE :")
        if inpt != "":
            pass
        import subprocess;subprocess.call("cls",shell=True)
        useroption()

    elif In == "5":
        import subprocess;subprocess.call("cls && py users.py",shell=True)

useroption()