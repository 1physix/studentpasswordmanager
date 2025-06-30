from time import sleep
passwordmanager = {}

def main():
    opt = input("""Welcome to Student Password Manager!
                1 -> Add username and password for website
                2 -> Get username and password
                
                >>>""")
    if opt == "1":
        create_password()
    elif opt == "2":
        get_password()
    else:
        print("Please enter a valid choice!")

def create_password():
    site = input("Enter website name: ")
    
    if site in passwordmanager:
        replace = input(f"The website {site}.com already has a login stored. Would you like to rewrite it (Yes or No)? -> ")
        if replace == "Yes":
            username = input("Enter username: ")
            password = input("Enter password: ")
            passwordmanager[site] = [username, password]
            print("Details saved!")
            sleep(1)
            main()
        else:
            main()
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    passwordmanager[site] = [username, password]
    print("Details saved!")
    sleep(1)
    main()

def get_password():
    name = input("Enter website name: ")
    try:
        lst = passwordmanager[name]
        print(f"""Username = {lst[0]}
Password = {lst[1]}
""")
    except:
        print("No details for that website! ")
     
    main()

main()