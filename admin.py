from store import printdatabase
#For admin use only
Admin = input("Enter your admin password: ")
if Admin == "admin":
    print("Welcome to the admin page")
    choice = input("Do you want to see the database? (y/n)")
    if choice == "y":
        printdatabase()
    else:
        exit()
else:
    print("You are not an admin")
    exit()
