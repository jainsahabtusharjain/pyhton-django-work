import _sqlite3

database = "users.db"
connection = _sqlite3.connect(database)
cursorobject = connection.cursor()
print("\t\tYOUR CURRENT DATABASE IS "+database+"!"+" of sqlite3\n\n")

cursorobject = connection.cursor()
cursorobject.execute("CREATE TABLE IF NOT EXISTS users (FirstName varchar(50) unique not null,LastName TEXT not null,City TEXT not null)")

connection.commit()
def useroption():
    print("Please choose What You Want to Do :"+"\n")
    print("\t1:CREATE\t2:READ\t\t3:UPDATE\t4:DELETE\t5:Quit\n")
    In = input("Your Choice :")

    if In == "1":
        E = "Y"
        while E in "Yy":
            val = (
                input("FirstName :"),
                input("LirstName :"),
                input("City :")
                )
            sql = "INSERT INTO users (FirstName,LastName,City) VALUES(?, ?, ?)"
            try:
                cursorobject.execute(sql, val)
                connection.commit()
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
                import subprocess;subprocess.call("cls && py chsqlite3.py",shell=True)
            else:
                for x in myresult:
                    print(x)
            #connector.commit()
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
                sql = "update users set FirstName=? where FirstName=?"
                try:
                    cursorobject.execute(sql,(updatename,fname))
                    connection.commit()
                    print("Updated Sucessfuly !")
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
                sql = "update users set LastName=? where LastName=?"
                try:
                    cursorobject.execute(sql,(updatelname,lname))
                    print("Updated Sucessfuly !")
                    connection.commit()
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
                sql = "update users set FirstName=? where FirstName=?"
                try:
                    cursorobject.execute(sql,(updatedcity,cityname))
                    print("Updated Sucessfuly !")
                    connection.commit()
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
            sql = "DELETE FROM users WHERE FirstName =?"
            try:
                cursorobject.execute(sql,(delname,))
                connection.commit()
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