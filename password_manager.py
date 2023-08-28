master_password = input("What would you like your master password to be? ")

userfile = input("What would you like your file name to be? ")

# class exception to be raised
class InvalidInput(Exception):
    """Raised when the user does not input a valid option"""
    pass

#allows user to view existing passwords
def view(master_password):
    """
    Prompts the user to re-enter the master password and prints the stored passwords.

    Args:
        master_password (str): The master password to be verified.

    Raises:
        InvalidInput: If the entered master password does not match the predefined master password.

    """
    re_master_password = input("Please re-enter previously defined master password: ")

    if re_master_password != master_password:
        raise InvalidInput("Incorrect master password, please try again")

    passwords = []
    with open(userfile+".txt", 'r') as file:
        for line in file:
            user, passw = line.strip().split("|")
            passwords.append({"User": user, "Password": passw})

    print(passwords)

#allows user to add a new password
def add():
    name = input('Account name: ')
    pwd = input("Password: ")
    #Manually closes file after use with an exception handle
    try:
        with open(userfile+".txt", 'a') as file:
            file.write(name + " | " + pwd + '\n')
        return "Success"
    except Exception as e:
        print("An error occured while writing to the file:", str(e))


while True:
    user_option = input("Would you like to add a new password or view them ('view' or 'add')? Press q to quit. ").lower()
    if user_option == 'q':
        break

    try:
        if user_option == "view":
            view(master_password)
        elif user_option == "add":
            add()
        else:
            raise InvalidInput
    except InvalidInput:
        print("Invalid Input")
        print("Please try again.")