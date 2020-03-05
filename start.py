#page 83 in Python Magazine

import time
users = {}
status = ""

def mainMenu():
    
    status = input("Do you have a login account? y/n Or press q to quit.")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    elif status == "q":
        quit()

def newUser():
    createLogin = input("Create a login name: ")

    if createLogin in users:
        print("\nSorry, that login name already exists. Please try a different one.\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created!\n")
        logins = open("C:/Users/Luis Castillo/Documents/logins.txt", "a")
# Menno, change the path shown in the previous line so the file logins.txt
# can be found in your computer
        logins.write("\n" + createLogin + " " + createPassw)
        logins.close()

def oldUser():
    login = input("Enter the login name: ")
    passw = input("Enter password: ")

#Check if user exists and login matches password

    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
        print("User: ", login, "accessed the system on: ", time.asctime())
    else:
        print("\nUser doesn't exist or wrong password!\n")

while status != "q":
    status = mainMenu()

    
