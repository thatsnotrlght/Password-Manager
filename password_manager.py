master_password = input("What would you like your master password to be? ")

# class exception to be raised
class InvalidInput(Exception):
    "Raised when the user does not input valid option"
    pass


#allows user to view existing passwords
def view():
    masterpwd = input("Please re-enter previously defined master password: ")

    if masterpwd != master_password:
        print("Incorrect master password, please try again")
    else:
        with open('passwords.txt', 'r') as file:
            line = file.readline() #initial prime read for while loop
            while line:
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:", user + " | " + "Password:", passw)
                line = file.readline() #reassigns line to next line of file
        

#allows user to add a new password
def add():
    name = input('Account name: ')
    pwd = input("Password: ")

    #Manually closes file after use
    with open('passwords.txt', 'a') as file:
        file.write(name + " | " + pwd + '\n')


while True:
    user_option = input("Would you like to add a new password or view them ('view' or 'add')? Press q to quit. ").lower()
    if user_option == 'q':
        break

    try:
        if user_option == "view":
            view()
        elif user_option == "add":
            add()
        else:
            raise InvalidInput
    except InvalidInput:
        print("Invalid Input")
        print("Please try again.")