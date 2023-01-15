print("<----Welcome You Here---->")

def useroption():
    print("\nplease choose your prefered Database\n")
    print("\tPress 1 for MySQL")
    print("\tPress 2 for Sqlite3")
    print("\tPress 3 for Postgresql\n")
    userchoice= input("Database You want to use :")
    return userchoice

uo=useroption()
if uo=="1":
    import subprocess;subprocess.call("cls",shell=True)
    import mysqldb

elif uo == "2":
    import subprocess;subprocess.call("cls",shell=True)
    import chsqlite3

elif uo == "3":
    import subprocess;subprocess.call("cls",shell=True)
    import nfpost
